# Simple RAG Chatbot with Langchain

## Overview
The goal of this project is to develop a **domain-specific application** that combines the strengths of a **Large Language Model (LLM)** with the **efficiency of a vector database** for data storage and retrieval. Using **Retrieval-Augmented Generation (RAG)** for the method and **Streamlit** for the front-end, the application is built with Python.

## Technology Stack:
- **Frontend**: Streamlit for building the user interface.
- **Vector Database**: Pinecone for efficient data storage and retrieval. 
- **LLM**: Huggingface model and gemma model using ollama
- **Backend**: LangChain framework utilizing the RAG method.

## Project Structure
- **src/**: Contains Python-based chatbot script and Streamlit main script.
- **src/materials/**: Contains data that our model will use to answer questions.
- **report/**: Stores [Report](report) files.

- **.env**: Contains API keys.

## Dependencies
- Python 3.12
- langchain
- FAISS-Client
- python-dotenv
- streamlit
- Text data

## Usage
1. Clone the repository: `git clone https://github.com/Faridghr/Simple-RAG-Chatbot.git`
2. Navigate to the project directory: `cd Simple-RAG-Chatbot`
3. Install dependencies: `pip install -r requirements.txt`
4. Set up your LLM.
5. Set up your Hugging Face api key in '.env
5. Navigate to src directory: `cd src`
6. Run the Streamlit application: `streamlit run streamlitMain.py`
7. Open your web browser and navigate to the URL provided by Streamlit (usually http://localhost:8501).
8. Interact with the chatbot by typing messages and receiving responses from the local LLM service.

9.Provided the api key in .env file


