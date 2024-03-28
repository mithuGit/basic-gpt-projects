import openai

openai.api_key = "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",

def chat_with_gpt3(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.0-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].text.strip()


if __name__ == "__main__":
    print("Welcome to your own GPT-3 Chatbot!")
    print("To end the conversation, type 'exit', 'quit' or 'bye'and press Enter.")
    print("="*50)
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            break
        response = chat_with_gpt3(user_input)
        print(f"Chatbot: {response}")
        print("="*50)