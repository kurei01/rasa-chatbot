import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Define a function to process user input
def process_input(input_text):
    doc = nlp(input_text)
    intent = None

    # Check if the input contains a specific intent
    if "greeting" in input_text:
        intent = "greeting"
    elif "goodbye" in input_text:
        intent = "goodbye"
    elif "thanks" in input_text:
        intent = "thanks"

    return intent

# Main loop
while True:
    # Get user input
    user_input = input("User: ")

    # Process the input
    intent = process_input(user_input)

    # Handle different intents
    if intent == "greeting":
        print("Bot: Hello! How can I help you?")
    elif intent == "goodbye":
        print("Bot: Goodbye! Have a nice day!")
        break  # Exit the loop
    elif intent == "thanks":
        print("Bot: You're welcome!")

    # Add more intents and responses as needed