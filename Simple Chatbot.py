import re

class SimpleChatbot:
    def __init__(self):
        self.context = {}

    def greet(self):
        return "Hello! I'm a simple chatbot created by Vasanth. How can I help you today? Make spellings correct please"

    def farewell(self):
        return "Goodbye! If you have more questions, feel free to ask."

    def respond_to_greeting(self):
        return "Hi there! How can I assist you?"

    def respond_to_question(self, question):
        qa_pairs = {
            "What is your name?": "I'm Vasanth's chatbot.",
            "How are you?": "I'm just a program, so I don't have feelings, but thanks for asking!",
            "What do you do?": "I'm here to assist and answer your questions.",
            "Who created you?": "I was created by Vasanth using Python.",
            "Can you tell a joke?": "Sure! Why don't scientists trust atoms? Because they make up everything!",
            "What's the meaning of life?": "The meaning of life is subjective and varies from person to person.",
            "Tell me a fun fact.": "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!",
            "How do I stay motivated?": "Setting achievable goals, finding inspiration, and taking breaks can help you stay motivated.",
            "What's the weather like today?": "I'm sorry, I don't have real-time information. You can check a weather website or app for the current conditions.",
            "Tell me about yourself.": "I'm just a computer program designed to chat with users and answer questions. What would you like to know?",
            "Can you recommend a book?": "Certainly! What genre are you interested in, and I can suggest a book.",
            "How can I learn programming?": "You can start by learning the basics of a programming language like Python. There are many online resources and tutorials available.",
            "What's your favorite color?": "I don't have preferences, but many people like blue or green. What's your favorite color?",
        }

        if question in qa_pairs:
            return qa_pairs[question]
        else:
            return "I'm not sure how to answer that. Can you ask me something else?"

    def ask_user_questions(self):
        for i in range(3):
            user_response = input("Bot: Ask me a question: ")
            self.context[f"Question_{i+1}"] = user_response
            print(f"Bot: That's interesting! Tell me more about {user_response}.")

    def handle_user_input(self, user_input):
        if re.search(r'\b(hi|hello|hey)\b', user_input, re.IGNORECASE):
            return self.respond_to_greeting()
        elif re.search(r'\b(bye|goodbye)\b', user_input, re.IGNORECASE):
            return self.farewell()
        elif "?" in user_input:
            return self.respond_to_question(user_input)
        else:
            return "I'm not sure how to respond. Can you rephrase that?"

    def chat(self):
        print(self.greet())

        while True:
            user_input = input("User: ")
            if re.search(r'\b(exit|quit)\b', user_input, re.IGNORECASE):
                print(self.farewell())
                break

            response = self.handle_user_input(user_input)
            print(f"Bot: {response}")

if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.chat()
