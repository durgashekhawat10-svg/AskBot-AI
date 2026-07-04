import gradio as gr
from chatbot import chatbot


def respond(message):
    return chatbot(message)


interface = gr.Interface(
    fn=respond,
    inputs=gr.Textbox(
        placeholder="Ask your question here..."
    ),
    outputs="text",
    title="AI FAQ Chatbot",
    description="Ask questions related to Artificial Intelligence"
)

interface.launch()