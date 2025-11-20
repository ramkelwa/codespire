import google.generativeai as genai

genai.configure(api_key="AIzaSyCns7hLBQAk-KpyZP84IYPrHZvtTreRgLs")

model = genai.GenerativeModel("models/gemini-flash-latest")

def explain_code_from_file(file_path):
    # Read code from file
    try:
        with open(file_path, "r") as f:
            code = f.read()
    except FileNotFoundError:
        return " Error: File not found. Please enter a valid file path."
    except Exception as e:
        return f" Error reading the file: {e}"

    # Send to Gemini
    response = model.generate_content(f"Explain this code simply:\n{code}")
    return response.text

file_path = input("Enter file path:\n")
print(explain_code_from_file(file_path))
