from openai import OpenAI

client = OpenAI(
    api_key="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",
    base_url="https://api.groq.com/openai/v1"
)

while True:
    user_input = input("You: ")
    if user_input == "quit":
        print("bot: Goodbye!")
        break
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "user", "content": "You are a medical bot ,provide information only related to medical"},
            {"role": "user", "content": user_input}
        ]
    )
    print("Bot:", response.choices[0].message.content)
