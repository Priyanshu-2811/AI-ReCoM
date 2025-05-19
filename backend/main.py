from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from context_store import store_context, get_context
from gemini_client import summarize_text, ask_question
from auth import signup, login
import fitz  # PyMuPDF

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class QnARequest(BaseModel):
    user_id: str
    question: str

@app.post("/signup")
async def signup_user(username: str = Form(...), password: str = Form(...)):
    if signup(username, password):
        return {"message": "Signup successful", "user_id": username}
    return {"error": "User already exists"}

@app.post("/login")
async def login_user(username: str = Form(...), password: str = Form(...)):
    if login(username, password):
        return {"message": "Login successful", "user_id": username}
    return {"error": "Invalid credentials"}

@app.post("/upload_pdf/")
async def upload_pdf(user_id: str = Form(...), file: UploadFile = Form(...)):
    pdf = await file.read()
    doc = fitz.open(stream=pdf, filetype="pdf")
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    summary = summarize_text(full_text)
    store_context(user_id, {"text": full_text, "summary": summary})
    return {"summary": summary}

@app.post("/ask")
async def ask(req: QnARequest):
    context = get_context(req.user_id)
    if not context:
        return {"answer": "No context found. Please upload a paper first."}
    text = context.get("text", "")
    full_prompt = f"Context: {text}\n\nQuestion: {req.question}"
    answer = ask_question(full_prompt)
    return {"answer": answer}
