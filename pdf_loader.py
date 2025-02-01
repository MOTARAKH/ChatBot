from langchain_community.document_loaders import PyPDFLoader

def load_pdfs(file_paths):
    """
    Load and extract text from multiple PDF files.
    Args:
        file_paths (list): List of paths to the PDF files.
    Returns:
        list: List of Document objects containing the extracted text.
    """
    documents = []
    for file_path in file_paths:
        try:
            loader = PyPDFLoader(file_path)
            docs = loader.load()
            documents.extend(docs)
            print(f"Extracted Text from {file_path}:")
            for doc in docs:
                print(doc.page_content)
        except Exception as e:
            print(f"Error loading PDF {file_path}: {e}")
            raise
    return documents