def answer_question(vectorstore, query):
    """
    Find the best matching answer for a given question in both English and Arabic.
    Args:
        vectorstore (FAISS): The FAISS vectorstore.
        query (str): The user's question.
    Returns:
        str: The closest matching answer or a fallback message.
    """
    try:
        print(f"Received query: {query}")
        # Retrieve the top result based on similarity
        results = vectorstore.similarity_search(query, k=1)
        print(f"Search results: {results}")

        if results:
            # Extract the document content
            document_content = results[0].page_content

            # Find the matching question and answer
            lines = document_content.split("\n")
            for i, line in enumerate(lines):
                if query.lower() in line.lower():
                    # Extract the answer (assumes the answer follows the question)
                    if i + 1 < len(lines) and (lines[i + 1].startswith("Answer:") or lines[i + 1].startswith("الإجابة :")):
                        return lines[i + 1].replace("Answer:", "").replace("الإجابة :", "").strip()

            # Fallback if no specific answer is found
            return "Sorry, I couldn't find a direct answer to your question."
        else:
            return "Sorry, I couldn't find an answer to your question."
    except Exception as e:
        print(f"Error during similarity search: {e}")
        raise