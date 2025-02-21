import pytest
from src.nlp.topic_modeling import extract_topics

def test_extract_topics():
    conversation = [
        {"role": "user", "text": "Hola, necesito ayuda con mi pago"},
        {"role": "agent", "text": "Claro, ¿podrías darme más detalles?"},
        {"role": "user", "text": "No puedo ver mi factura en la plataforma"}
    ]
    
    expected_topics = ["Facturación", "Pagos", "Problemas de acceso"]
    topics = extract_topics(conversation)
    
    assert isinstance(topics, list)
    assert all(topic in expected_topics for topic in topics)
    assert len(topics) > 0

def test_extract_topics_empty_conversation():
    conversation = []
    
    topics = extract_topics(conversation)
    
    assert topics == []