from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
def create_vectorstore(documents):
    """
    Create a FAISS vectorstore using HuggingFaceEmbeddings.
    Args:
        documents (list): List of `Document` objects.
    Returns:
        FAISS: A FAISS vectorstore for similarity search.
    """
    try:
        # Initialize HuggingFace embeddings
        print("Loading HuggingFace Embeddings...")
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

        # Split documents into smaller chunks
        print("Splitting documents...")
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        split_docs = text_splitter.split_documents(documents)

        # Extract text from split documents
        texts = [doc.page_content for doc in split_docs]

        # Create FAISS vectorstore
        print("Creating FAISS vectorstore...")
        vectorstore = FAISS.from_texts(texts=texts, embedding=embeddings)
        print("FAISS vectorstore created successfully!")
        return vectorstore

    except Exception as e:
        print(f"Error during vectorstore creation: {e}")
        raise