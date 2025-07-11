# Learnix
AI Powered Interactive Learning Assistant for Classrooms
# Problem Statement
Modern classrooms lack real-time, interactive tools to address diverse student needs and keep them engaged. The objective is to create a multimodal AI assistant that:

1. Accepts and processes text, voice, and visual queries from students in real-time.
2. Provides contextual responses, including textual explanations, charts, and visual aids.
3. Detects disengagement or confusion using facial expression analysis and suggests interventions.

# Uniquenss of the Project
Learnix is a smart AI-based learning assistant that allows students to ask questions through text, voice, or images. It uses advanced technologies like OCR for extracting text from images and speech recognition for voice input, making learning more interactive and accessible. This multimodal approach supports different learning styles and helps students engage more effectively.

The system is powered by Intel’s NeuralChat model optimized with OpenVINO™, ensuring fast and efficient performance even on standard CPUs. Its lightweight design and user-friendly web interface make it ideal for classrooms with limited resources. Learnix is a flexible and scalable solution for personalized, AI-enhanced learning.

# Overview 
Learnix is a smart, AI-powered interactive learning assistant developed to support classroom and self-learning environments. It offers a multimodal interface where users can interact using text input, voice queries, or by uploading images of printed or handwritten academic content. By combining Natural Language Processing (NLP), Optical Character Recognition (OCR), and speech recognition, Learnix provides a flexible and accessible solution tailored to different student needs. The system is powered by Intel's NeuralChat model, optimized using OpenVINO™, and deployed via a lightweight Flask backend with a clean, user-friendly web interface.

# Outcomes
The project successfully delivers a responsive and efficient AI learning assistant capable of answering academic queries in real time. It demonstrates strong performance across different input types, especially text and printed image queries, with over 90% OCR accuracy on clean inputs. The integration of OpenVINO™ ensures that the model performs efficiently on CPU-based systems without requiring GPU acceleration, making the tool highly suitable for low-resource educational settings. The voice processing logic is implemented in the backend, and the frontend provides a seamless experience for entering questions and receiving responses.

# Limitations
Despite its strong performance, Learnix has a few limitations. The voice input feature is currently functional only in the backend and not integrated into the frontend due to UI constraints. OCR accuracy significantly drops when processing poorly lit, skewed, or handwritten text. Additionally, the system lacks advanced interaction features such as context retention for follow-up questions or dynamic conversation flows, which could enhance its usability in complex learning scenarios.

# Future Scope
The project has considerable potential for expansion. Future enhancements include integrating full frontend voice support, improving OCR performance for handwritten and noisy text, and adding conversational memory for multi-turn question-answering. The system can also be deployed on edge devices for offline use, benefiting areas with limited internet access. Incorporating multilingual support, personalized learning feedback, and integration with educational databases can further elevate Learnix into a comprehensive AI tutor for diverse learning environments.
