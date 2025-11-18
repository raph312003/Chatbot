import customtkinter as ctk

#Fonction chatbot pour nous répondre

def chatbot_response(user_input):
    responses ={
        "bonjour":"Bonjour ! Comment puis je vous aider ?",
        "comment ca va ?":"Je suis un programme, donc je vais toujours bien",
        "quelle heure est il": "Je peux pas dire mais il est temps de coder ?",
        "au revoir": "Au revoir passez une excellente journée !"
    }
    return responses.get(user_input.lower(), "Désolé je ne comprends pas votre question")

#fonction pour gérer l'envoie du message
def send_message(event=None):
    user_message= user_input.get()
    if user_message.strip()!="":
        chat_history.configure(state="normal")
        chat_history.insert("end", f"Vous :{user_message}\n","user")
        bot_response = chatbot_response(user_message)
        chat_history.insert("end",f"chatbot:{bot_response}\n", "bot")
        chat_history.configure(state="disabled")
        chat_history.see("end")
        user_input.delete(0,"end")


# Interface
app=ctk.CTk()
app.geometry("500*600")
app.title("Chatbot ETCSCHOOL")

# en-tete
header =ctk.CTkLabel(app, text= "Bienvenue sur le chatbot de ETCSHOOL", font=("Arial",18,"bold"))
header.pack(pady=10)

# Zone d'affichage message
chat_history = ctk.CTkTextbox(app, height=400, state='disabled')
chat_history.tag_config("user",foreground="black")
chat_history.tag_config("bot",foreground="green")
chat_history.pack(pady=10,padx=10, fill="both",expand =True)
chat_history.configure(font=("Arial",16))
# champ de saisi utilisateur

user_input_frame=ctk.CTkFrame(app)
user_input_frame.pack(pady=10,padx=10, fill="x")

user_input=ctk.CTkEntry(user_input_frame, placeholder_text=" Entrez votre text ici", width=350)
user_input.pack(side="left", padx=5)

send_button =ctk.CTkButton(user_input_frame, text="Envoyer", command=send_message)
send_button.pack(side="left")

#Associer la touche entrer à la fonction

app.bind("<Return>",send_message)


app.mainloop()
