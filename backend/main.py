from fastapi import FastAPI, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chatbot import Chatbot

app = FastAPI()
chatbot = Chatbot(data_dir="data")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    message: str

@app.post("/chat")
async def chat(query: Query):
    answer = chatbot.handle_message(query.message)
    return {"reply": answer}
