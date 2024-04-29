from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.openai_chat import get_response_from_openai, get_prompt
from src.google_form_response_reader import get_student_proficiency_by_id, get_student_class_by_id
from src.youtube_video_summarizer import get_youtube_video_summary


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

class YoutubeSummaryRequest(BaseModel):
    youtube_video_url: str


@app.post("/ask", response_model=Response)
async def ask_question(request: QuestionRequest):
    student_proficiency = get_student_proficiency_by_id(id=int(request.user_id))
    student_class = get_student_class_by_id(id=int(request.user_id))
    prompt = get_prompt(request.subject, student_class, student_proficiency)
    # pr = "You are a science teacher. Your user is a 9th grade student from India who has beginner level understanding of science subject. You must answer all the questions in this template - Intro: Welcome to our application! As a beginner, we'll provide explanations in easy terms to help you grasp the concepts better. Let's dive into it! Answer/Explanation: Today, let's talk about [Concept]. It's essentially [Brief Explanation]. For example, think of it like [Real World Example 1], or [Real World Example 2]. Doubts: Do you have any doubts about this concept? Feel free to ask!"
    response = get_response_from_openai(prompt = prompt, question= request.question)
    return {"answer": response.content}


@app.post("/youtubeVideoSummary", response_model=Response)
async def generate_youtube_summary(request: YoutubeSummaryRequest):
    youtube_summary = get_youtube_video_summary(youtube_url=request.youtube_video_url)
    return {"answer": youtube_summary}