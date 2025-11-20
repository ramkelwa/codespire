import google.generativeai as genai

# Put your API key here
genai.configure(api_key="YOUR_ACTUAL_API_KEY")

model = genai.GenerativeModel("gemini-1.5-pro")

print("AI Ready! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    response = model.generate_content(user_input)
    print("AI:", response.text, "\n")