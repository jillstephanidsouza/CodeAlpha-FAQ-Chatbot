import re
from difflib import SequenceMatcher
print("Chatbot program started!")
# Frequently Asked Questions
faqs = {
    "what is codealpha": "CodeAlpha is a technology company that offers internship opportunities.",
    "what is an internship": "An internship helps students gain practical experience and skills.",
    "how can i get a certificate": "Complete the required internship tasks and follow the submission instructions.",
    "how many tasks should i complete": "Check your internship instructions for the required number of tasks.",
    "what is python": "Python is a popular programming language used in many areas of software development.",
    "how can i contact codealpha": "You can visit www.codealpha.tech for more information.",
    "thank you": "You're welcome! Is there anything else I can help you with?"
}


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text.strip()


def find_answer(user_question):
    cleaned_question = clean_text(user_question)
    best_match = None
    best_score = 0

    for question in faqs:
        cleaned_faq = clean_text(question)
        score = SequenceMatcher(
            None, cleaned_question, cleaned_faq
        ).ratio()

        if score > best_score:
            best_score = score
            best_match = question

    if best_score >= 0.45:
        return faqs[best_match]

    return "Sorry, I don't know the answer. Please try asking another question."


print("================================")
print("       CODEALPHA FAQ CHATBOT")
print("================================")
print("Ask me a question!")
print("Type 'bye' to exit.")

while True:
    user_input = input("\nYou: ")

    if clean_text(user_input) in ["bye", "exit", "quit"]:
        print("Chatbot: Goodbye! Have a nice day!")
        break

    answer = find_answer(user_input)
    print("Chatbot:", answer)