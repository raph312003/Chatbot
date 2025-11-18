# from mistralai import Mistral
# import os

# client = Mistral(api_key="OWmuJ9IqHL3kUEnGDdDljc73bbEPxfX9") # Clé API mistral contacter les serveurs mistrals

# def chat_with_mistral(prompt):
#     response = client.chat.complete(
#         model="mistral-small-latest",
#         messages=[                      # Envoie une list message
#             {"role": "user", "content": prompt} # Message avec user et le text
#         ]
#     )
#     return response.choices[0].message.content #renvoie le text généré par l'IA


# if __name__ == "__main__":
#     while True:
#         user_input = input("You: ") # Prend en compte se que je tape dans le terminal
#         if user_input.lower() in ["quit", "exit", "bye"]:
#             break

#         reply = chat_with_mistral(user_input) # appelle chatgpt with mistral
#         print("Chatbot:", reply)


import gradio as gr                                     # Faire un chat lunch
import requests

API_URL = "https://api.mistral.ai/v1/chat/completions"
API_KEY = "OWmuJ9IqHL3kUEnGDdDljc73bbEPxfX9"

# ---- ICI : tu définis le ton, la personnalité, les règles ---- créer un fichier memory.json
SYSTEM_PROMPT = """                                
Tu es CoachRaph : clair, direct, sans langue de bois.
Tu expliques simplement, tu gardes un ton humain et précis.
Pose une question si la demande n’est pas assez précise.
"""

def chat(message, history):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    data = {
        "model": "mistral-small-latest",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},   # <-- TON PERSONNALISÉ
            {"role": "user", "content": message}
        ]
    }
    r = requests.post(API_URL, json=data, headers=headers)
    print("DEBUG:", r.json())
    return r.json()["choices"][0]["message"]["content"]
    


gr.ChatInterface(chat).launch()

