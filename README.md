# AskBot AI

**AskBot AI** is an intelligent FAQ chatbot built using **Python**, **Natural Language Processing (NLP)**, **NLTK**, **Scikit-learn**, and **Gradio**. It is designed to answer frequently asked questions by understanding user input and matching it with the most relevant question from a predefined knowledge base using **TF-IDF Vectorization** and **Cosine Similarity**.

This project demonstrates the practical application of NLP techniques for building an interactive and efficient FAQ chatbot.

---

##  Overview

AskBot AI is a rule-based intelligent chatbot that answers user queries by finding the most similar question from a collection of Frequently Asked Questions (FAQs).

Unlike traditional keyword-based systems, AskBot AI preprocesses user input, converts text into numerical vectors using TF-IDF, and applies Cosine Similarity to identify the closest matching question. This approach enables the chatbot to understand different ways of asking the same question and deliver accurate responses.

---

## Features

-  AI-powered FAQ chatbot
-  Natural Language Processing (NLP)
-  Text preprocessing using NLTK
-  Tokenization and stopword removal
-  TF-IDF Vectorization
-  Cosine Similarity for intelligent question matching
-  Interactive web interface using Gradio
-  Fast and lightweight implementation
-  Easily expandable FAQ database
-  Beginner-friendly project structure

---

##  Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| NLTK | Text preprocessing |
| Scikit-learn | TF-IDF Vectorization & Cosine Similarity |
| Gradio | Interactive chatbot interface |

---

## Project Structure

```
AskBot-AI/
│--  LICENSE
|--  README.md            # Project documentation
|--  app.py               # Gradio user interface
|--  chatbot.py           # NLP processing and chatbot logic
|--  faq_data.py          # FAQ questions and answers
|--  requirements.txt     # Required Python packages
|--  screenshots          #display the outcomes
```

---

##  How It Works

### Step 1: User Enters a Question

Example:

```
What is Artificial Intelligence?
```

↓

### Step 2: Text Preprocessing

The chatbot performs:

- Convert text to lowercase
- Tokenization
- Remove punctuation
- Remove stopwords

Example:

```
What is Artificial Intelligence?
```

↓

```
artificial intelligence
```

↓

### Step 3: TF-IDF Vectorization

The cleaned text is transformed into numerical vectors using **TF-IDF (Term Frequency–Inverse Document Frequency)**.

↓

### Step 4: Cosine Similarity

The user's question is compared with every FAQ question.

The chatbot calculates similarity scores and identifies the closest match.

↓

### Step 5: Generate Response

If the similarity score is above the threshold, the corresponding answer is displayed.

Otherwise:

```
Sorry, I couldn't understand your question.
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/durgashekhawat10-svg/AskBot-AI.git
```

### 2. Navigate to the Project Directory

```bash
cd AskBot-AI
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

##  Usage

Run the application:

```bash
python app.py
```

After execution, Gradio will generate a local URL similar to:

```
http://127.0.0.1:7860
```

Open the link in your web browser to interact with the chatbot.

---

##  Sample Questions

Try asking:

- What is Artificial Intelligence?
- What is Machine Learning?
- Explain Deep Learning.
- What is Python?
- What is NLP?
- What is TensorFlow?
- What is Data Science?
- What is Computer Vision?
- What is Generative AI?
- What is a Chatbot?
 and many more
---

##  Screenshots

Create a folder named **screenshots** inside the project directory and add images of the chatbot interface.

Example:

```
screenshots/
│
├── home_page.png
├── chatbot_response.png
└── sample_conversation.png
```

You can then display them in your README like this:


## Future Enhancements

-  Voice-enabled chatbot
-  Multi-language support
-  Database integration
-  User authentication
-  Chat history
-  Cloud deployment
-  Upload PDF and answer questions
-  Integration with Large Language Models (LLMs)
-  Mobile-friendly interface

---

## Requirements

- Python 3.10+
- NLTK
- Scikit-learn
- Gradio

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## Learning Outcomes

Through this project, you will understand:

- Natural Language Processing (NLP)
- Text preprocessing techniques
- Tokenization
- Stopword removal
- TF-IDF Vectorization
- Cosine Similarity
- Building an AI chatbot
- Creating web interfaces using Gradio
- Organizing Python projects

---

##  Author

**Durga Shekhawat**

If you found this project helpful, consider giving it a ⭐ on GitHub.

---
## Internship Project

This project was developed as part of the **Artificial Intelligence Internship Program** offered by **CodeAlpha**. The objective was to design and implement an AI-powered FAQ chatbot using Natural Language Processing (NLP) techniques, including text preprocessing, TF-IDF vectorization, and cosine similarity for intelligent question matching. 


## License

This project is licensed under the **MIT License**.

Feel free to use, modify, and distribute this project for educational and learning purposes.
