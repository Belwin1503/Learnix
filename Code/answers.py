import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
from transformers import AutoTokenizer
from optimum.intel.openvino import OVModelForCausalLM
from PIL import Image
import pytesseract

MODEL_PATH = "neural-chat/INT8"
DEVICE_TYPE = "CPU"

# Initialize tokenizer and OpenVINO model
text_tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
text_model = OVModelForCausalLM.from_pretrained(MODEL_PATH, device=DEVICE_TYPE, compile=False)

# Compile model
print("Initializing OpenVINO model compilation...")
text_model.compile()
print("Model compilation complete.")

# === Flask App Initialization ===
app = Flask(__name__, static_folder="frontend", static_url_path="/")
CORS(app)

# Upload folder config
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_DIR

# === Routes ===

@app.route("/")
def load_homepage():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:filepath>")
def serve_static_file(filepath):
    return send_from_directory(app.static_folder, filepath)

@app.route("/answerquery", methods=["POST"])
def process_text_input():
    payload = request.get_json()
    user_query = payload.get("question", "").strip()

    if not user_query:
        return jsonify({"answer": "No question provided."}), 400

    try:
        encoded_input = text_tokenizer(user_query, return_tensors="pt")
        generated_output = text_model.generate(**encoded_input, max_new_tokens=256)
        decoded_response = text_tokenizer.decode(generated_output[0], skip_special_tokens=True)
        return jsonify({"answer": decoded_response.strip()})
    except Exception as err:
        print("Text Processing Error:", err)
        return jsonify({"answer": "Error processing your question."}), 500

@app.route("/image-upload", methods=["POST"])
def process_image_input():
    if "image" not in request.files:
        return jsonify({"answer": "No image uploaded."}), 400

    image_file = request.files["image"]
    if image_file.filename == "":
        return jsonify({"answer": "No image selected."}), 400

    secure_name = secure_filename(image_file.filename)
    saved_path = os.path.join(app.config["UPLOAD_FOLDER"], secure_name)
    image_file.save(saved_path)

    try:
        with Image.open(saved_path) as img:
            detected_text = pytesseract.image_to_string(img, lang="eng").strip()

        if not detected_text:
            return jsonify({"answer": "No text found in image."})

        encoded_input = text_tokenizer(detected_text, return_tensors="pt")
        generated_output = text_model.generate(**encoded_input, max_new_tokens=256)
        decoded_response = text_tokenizer.decode(generated_output[0], skip_special_tokens=True)

        return jsonify({
            "answer": decoded_response.strip(),
            "extracted_text": detected_text
        })

    except Exception as err:
        print("OCR or Model Error:", err)
        return jsonify({"answer": "Error extracting or processing image text."}), 500

# === Run App ===
if __name__ == "__main__":
    app.run(debug=True, port=3000, threaded=True)
