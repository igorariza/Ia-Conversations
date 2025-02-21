import pytest
from src.nlp.sentiment_analysis import analyze_sentiment

def test_analyze_sentiment():
    conversation = {
        "conversation_id": "12345",
        "messages": [
            {"role": "user", "text": "Hola, necesito ayuda con mi pago"},
            {"role": "agent", "text": "Claro, ¿podrías darme más detalles?"},
            {"role": "user", "text": "No puedo ver mi factura en la plataforma"}
        ]
    }
    
    result = analyze_sentiment(conversation)
    
    assert result["conversation_id"] == "12345"
    assert len(result["sentiment_analysis"]) == 3
    assert result["average_sentiment"] in ["positive", "negative", "neutral"]
    assert any(msg["sentiment"] == "negative" for msg in result["sentiment_analysis"])  # Check for negative sentiment messages

def test_analyze_sentiment_empty():
    conversation = {
        "conversation_id": "12346",
        "messages": []
    }
    
    result = analyze_sentiment(conversation)
    
    assert result["conversation_id"] == "12346"
    assert result["sentiment_analysis"] == []
    assert result["average_sentiment"] == "neutral"  # Assuming neutral for empty conversation