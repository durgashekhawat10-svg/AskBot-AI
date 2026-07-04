import nltk
import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from faq_data import faq_data

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))


def preprocess(text):

    text = text.lower()

    tokens = word_tokenize(text)

    tokens = [
        word for word in tokens
        if word not in stop_words and word not in string.punctuation
    ]

    return " ".join(tokens)


questions = list(faq_data.keys())
answers = list(faq_data.values())

processed_questions = [preprocess(q) for q in questions]

vectorizer = TfidfVectorizer()

question_vectors = vectorizer.fit_transform(processed_questions)


def chatbot(user_question):

    processed_input = preprocess(user_question)

    input_vector = vectorizer.transform([processed_input])

    similarity = cosine_similarity(input_vector, question_vectors)

    best_index = similarity.argmax()

    score = similarity[0][best_index]

    if score > 0.30:
        return answers[best_index]
    else:
        return "Sorry, I couldn't understand your question."


if __name__ == "__main__":

    print("========== FAQ CHATBOT ==========")
    print("Type 'exit' to quit.\n")

    while True:

        question = input("You : ")

        if question.lower() == "exit":
            print("Bot : Goodbye!")
            break

        print("Bot :", chatbot(question))