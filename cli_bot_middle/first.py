import requests
import os

API_KEY = os.getenv("OPENAI_API_KEY")
url = "https://api.openai.com/v1/chat/completions"
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

messages = [{"role": "system", "content": "You are a helpful assistant."}]

while True:
    user_input = input("You: ")
    messages.append({"role": "user", "content": user_input})

    data = {
        "model": "gpt-3.5-turbo",
        "messages": messages
    }

    response = requests.post(url, headers=headers, json=data)
    answer = response.json()['choices'][0]['message']['content']

    print("Bot:", answer)
    messages.append({"role": "assistant", "content": answer})