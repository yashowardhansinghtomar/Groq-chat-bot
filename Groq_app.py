import gradio as gr
from groq import Groq

# Initialize the Groq client
client = Groq(
    api_key="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",
)

def generate_chat_completion(system_message, user_message):
    # Generate chat completion
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system_message,
            },
            {
                "role": "user",
                "content": user_message,
            }
        ],
        model="llama3-70b-8192",
    )
    
    return chat_completion.choices[0].message.content

# Define the Gradio interface
iface = gr.Interface(
    fn=generate_chat_completion,
    inputs=[
        gr.components.Textbox(lines=1, placeholder="System Message"),
        gr.components.Textbox(lines=5, placeholder="User Message")
    ],
    outputs=gr.components.Textbox(),
    title="Python Trainer Chatbot",
    description="Enter system and user messages to get a response.",
    theme="light"  # Changed to a default theme
)

# Launch the Gradio interface
iface.launch() 