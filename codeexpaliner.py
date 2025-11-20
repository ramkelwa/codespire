import google.generativeai as genai

genai.configure(api_key="AIzaSyCns7hLBQAk-KpyZP84IYPrHZvtTreRgLs")

model = genai.GenerativeModel("models/gemini-flash-latest")

def explain_code(code):
    response = model.generate_content(f"Explain this code simply:\n{code}")
    return response.text

print(explain_code(input("Enter code:\n")))
