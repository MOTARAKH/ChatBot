def reverse_text(text):
    """
    Reverse the text to fix the reversed Arabic text.
    """
    return text[::-1]

def extract_qa_pairs(text):
    """
    Extract questions and answers from the text.
    """
    qa_pairs = []
    lines = text.split("\n")
    question = None
    answer = None

    for line in lines:
        if "السؤال :" in line:
            question = line.split(":")[-1].strip()  # Extract the question after the colon
        elif "الإجابة :" in line:
            answer = line.split(":")[-1].strip()  # Extract the answer after the colon
            if question and answer:
                qa_pairs.append((question, answer))
                question = None
                answer = None

    return qa_pairs