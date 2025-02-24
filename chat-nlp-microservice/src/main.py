import sys
import openai
from dotenv import load_dotenv
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import json
import uuid
from nlp.sentiment_analysis import analyze_sentiment
from nlp.intent_detection import detect_intent
from nlp.topic_modeling import extract_topics
from nlp.summarization import generate_summary

load_dotenv()
openai.api_key = os.getenv("API_KEY")
app = FastAPI()
origins = [
    "http://localhost:4200",
    "http://localhost",
    "http://localhost:8000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Message(BaseModel):
    role: str
    text: str
    timestamp: str

class Conversation(BaseModel):
    conversation_id: str
    messages: List[Message]

@app.post("/process_conversation/")
async def process_conversation(conversation: Conversation):
    try:
        if not conversation.conversation_id:
            conversation.conversation_id = str(uuid.uuid4())

        messages_text = [message.text for message in conversation.messages]
        sentiment_results = analyze_sentiment(messages_text)
        intent_results = detect_intent(messages_text)
        topic_results = extract_topics(messages_text)
        summary_results = generate_summary(conversation.conversation_id, messages_text)

        return {
            "conversation_id": conversation.conversation_id,
            "sentiment_analysis": sentiment_results,
            "intentions": intent_results,
            "topics": topic_results,
            "summary": summary_results
        }
    except Exception as e:
        print("An error occurred: ", e)
        raise HTTPException(status_code=500, detail=str(e))