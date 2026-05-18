import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_chat_response(message):
    prompt = f"You are a kind, empathetic mental health assistant.\nUser: {message}\nAI:"
    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return res['choices'][0]['message']['content']
