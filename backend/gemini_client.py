import google.generativeai as genai

genai.configure(api_key="AIzaSyAqUHNCA0L6a6H9PWOSbJbns4JaAIu1wyI")

def summarize_text(text: str) -> str:
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"Summarize this academic paper:\n\n{text}")
    return response.text

def ask_question(prompt: str) -> str:
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text
