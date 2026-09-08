from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv


class ChatBot:

    load_dotenv()

    def __init__(self):

        # 1. Load document
        loader = TextLoader(
            "./materials/germany_travel_guide.txt"
        )

        documents = loader.load()

        # 2. Split document into chunks
        text_splitter = CharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=50
        )

        docs = text_splitter.split_documents(documents)

        # 3. Create Hugging Face embeddings
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        # 4. Create FAISS vector store
        docsearch = FAISS.from_documents(
            docs,
            embeddings
        )

        # 5. Create retriever
        retriever = docsearch.as_retriever()

        # 6. Initialize Ollama
        llm = ChatOllama(
            model="gemma3",
            temperature=0
        )

        # 7. Create prompt
        template = """
        You are a Germany travel assistant.

        Use the following context to answer the question.
        If you don't know the answer, just say you don't know.

        Your answer should be short and concise,
        no longer than 2 sentences.

        Context:
        {context}

        Question:
        {question}

        Answer:
        """

        prompt = PromptTemplate(
            template=template,
            input_variables=["context", "question"]
        )

        # 8. Format retrieved documents
        def format_docs(docs):
            return "\n\n".join(
                doc.page_content for doc in docs
            )

        # 9. Create RAG chain
        self.rag_chain = (
            {
                "context": retriever | format_docs,
                "question": RunnablePassthrough()
            }
            | prompt
            | llm
            | StrOutputParser()
        )


# Test
if __name__ == "__main__":

    chatbot = ChatBot()

    print("Chatbot initialized successfully!")

    response = chatbot.rag_chain.invoke(
        "What is the capital of Germany?"
    )

    print("Answer:", response)