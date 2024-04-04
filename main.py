from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.openai_chat import get_response_from_openai


app = FastAPI()

# CORS setup
origins = ["*"]  # Allow requests from all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

class QuestionRequest(BaseModel):
    user_id: str
    subject: str
    question: str

class Response(BaseModel):
    answer: str


@app.post("/ask", response_model=Response)
async def ask_question(request: QuestionRequest):
    response = get_response_from_openai(prompt = "", question= "")
    return {"answer": response.content}
