from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
from nlp.sentiment_analysis import analyze_sentiment
from nlp.intent_detection import detect_intent
from nlp.topic_modeling import extract_topics
from nlp.summarization import generate_summary

app = FastAPI()

class Conversation(BaseModel):
    conversation_id: str
    messages: list

@app.post("/process_conversation/")
async def process_conversation(conversation: Conversation):
    try:
        sentiment_results = analyze_sentiment(conversation.messages)
        intent_results = detect_intent(conversation.messages)
        topic_results = extract_topics(conversation.messages)
        summary_results = generate_summary(conversation.messages)

        return {
            "conversation_id": conversation.conversation_id,
            "sentiment_analysis": sentiment_results,
            "intentions": intent_results,
            "topics": topic_results,
            "summary": summary_results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))