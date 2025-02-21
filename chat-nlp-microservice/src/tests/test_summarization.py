import pytest
from src.nlp.summarization import generate_summary

def test_generate_summary():
    conversation = {
        "conversation_id": "12345",
        "messages": [
            {"role": "user", "text": "Hola, necesito ayuda con mi pago", "timestamp": "2025-02-19T10:00:00Z"},
            {"role": "agent", "text": "Claro, ¿podrías darme más detalles?", "timestamp": "2025-02-19T10:01:00Z"},
            {"role": "user", "text": "No puedo ver mi factura en la plataforma", "timestamp": "2025-02-19T10:02:00Z"}
        ]
    }
    
    expected_summary = "El usuario reportó un problema con la visualización de su factura en la plataforma. Se le pidió más información."
    
    summary = generate_summary(conversation)
    
    assert summary['conversation_id'] == conversation['conversation_id']
    assert summary['summary'] == expected_summary

def test_generate_summary_with_redundant_messages():
    conversation = {
        "conversation_id": "12346",
        "messages": [
            {"role": "user", "text": "Hola, necesito ayuda con mi pago", "timestamp": "2025-02-19T10:00:00Z"},
            {"role": "user", "text": "Hola, necesito ayuda con mi pago", "timestamp": "2025-02-19T10:01:00Z"},
            {"role": "agent", "text": "Claro, ¿podrías darme más detalles?", "timestamp": "2025-02-19T10:02:00Z"},
            {"role": "user", "text": "No puedo ver mi factura en la plataforma", "timestamp": "2025-02-19T10:03:00Z"}
        ]
    }
    
    expected_summary = "El usuario reportó un problema con la visualización de su factura en la plataforma. Se le pidió más información."
    
    summary = generate_summary(conversation)
    
    assert summary['conversation_id'] == conversation['conversation_id']
    assert summary['summary'] == expected_summary

def test_empty_conversation():
    conversation = {
        "conversation_id": "12347",
        "messages": []
    }
    
    summary = generate_summary(conversation)
    
    assert summary['conversation_id'] == conversation['conversation_id']
    assert summary['summary'] == ""  # Assuming the summary should be empty for no messages.