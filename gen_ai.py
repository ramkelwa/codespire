import google.generativeai as genai

# 1) Configure API
genai.configure(api_key="YOUR_API_KEY_HERE")

# 2) Select model
model = genai.GenerativeModel("gemini-1.5-pro")

print("Your Basic Gen AI is Ready!")
print("Type 'exit' to stop.\n")

# 3) Chat loop
while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    response = model.generate_content(user_input)

    print("\nAI:", response.text, "\n")