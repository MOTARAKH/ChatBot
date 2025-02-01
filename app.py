import os
from flask import Flask, request, jsonify, render_template
from pdf_loader import load_pdfs
from vectorstore import create_vectorstore
from question_answer import answer_question
import traceback

# Flask app initialization
app = Flask(__name__)

# Initialize global variables
vectorstore = None
documents = None

def initialize_vectorstore():
    """
    Initializes the vectorstore by loading the PDFs and creating the FAISS vectorstore.
    """
    global vectorstore, documents
    try:
        # Load and process the PDFs
        print("Loading PDFs...")
        FILE_PATHS = ["data.pdf", "data2.pdf"]  # Add paths to your PDFs
        documents = load_pdfs(FILE_PATHS)

        # Check if documents were loaded
        if not documents:
            raise ValueError("No content extracted from the PDFs.")

        # Create the FAISS vectorstore
        print("Creating FAISS vectorstore...")
        vectorstore = create_vectorstore(documents)
        print("Vectorstore created successfully!")

    except Exception as e:
        print(f"Error during initialization: {e}")
        traceback.print_exc()
        vectorstore = None

# Initialize the vectorstore at the start
initialize_vectorstore()

@app.route("/")
def home():
    """
    Render the home page with the chat interface.
    """
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    """
    Handle user questions and return answers.
    """
    if vectorstore is None:
        return jsonify({"error": "The vectorstore could not be initialized. Please check the logs."}), 500

    user_question = request.form.get("question")
    if not user_question:
        return jsonify({"error": "Please enter a question."}), 400

    try:
        print(user_question)
        # Get the answer from the vectorstore
        response = answer_question(vectorstore, user_question)
        return jsonify({"answer": response})
    except Exception as e:
        # Log the error for debugging
        print(f"Error processing the question: {e}")
        traceback.print_exc()  # Print detailed error traceback
        return jsonify({"error": "An error occurred while processing your question. Please try again."}), 500

if __name__ == "__main__":
    app.run(debug=True)