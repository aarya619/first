def respond_to_user(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "your name" in user_input:
        return "I am a chatbot, and I don't have a personal name. But you can call me Chatbot!"
    elif "help" in user_input:
        return "I can help you with simple questions. Ask me 'how are you' or say 'hello' to start!"
    else:
        return "Sorry, I don't understand that. Can you try asking something else?"

def start_chat():
    print("Hello! I'm your friendly chatbot. Type 'bye' to end the conversation.")
    
    while True:
        user_input = input("You: ")

        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break

        response = respond_to_user(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    start_chat()
