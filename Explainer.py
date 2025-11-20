import google.generativeai as genai

genai.configure(api_key="AIzaSyD5R6zPWUbshkRu5hqGfkpJV7BzV8UyNow")

model = genai.GenerativeModel("gemini-1.5-flash")

def explain_code(code):
    response = model.generate_content(f"Explain this code simply:\n{code}")
    return response.text

print(explain_code(input("Enter code:\n")))
