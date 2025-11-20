import google.generativeai as genai

# 1. Configure Gemini with your API key
genai.configure(api_key="YOUR_API_KEY_HERE")

# 2. Load model
model = genai.GenerativeModel("gemini-1.5-pro")

print("Gemini Text Summarizer")
print("-----------------------")

# 3. Input long text
text = input("\nEnter the text you want to summarize:\n\n")

# 4. Ask Gemini to summarize
prompt = f"Summarize the following text in simple, short points:\n\n{text}"

response = model.generate_content(prompt)

# 5. Print summary
print("\nSummary:\n")
print(response.text)