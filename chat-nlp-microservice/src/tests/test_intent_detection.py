import pytest
from src.nlp.intent_detection import detect_intent

def test_detect_intent_support_request():
    message = "Necesito ayuda con mi cuenta"
    expected_intent = "Solicitud de soporte"
    assert detect_intent(message) == expected_intent

def test_detect_intent_complaint():
    message = "El servicio está fallando"
    expected_intent = "Queja"
    assert detect_intent(message) == expected_intent

def test_detect_intent_inquiry():
    message = "Quiero saber el estado de mi pedido"
    expected_intent = "Consulta"
    assert detect_intent(message) == expected_intent

def test_detect_intent_unknown():
    message = "Esto es un mensaje extraño"
    expected_intent = "Desconocido"
    assert detect_intent(message) == expected_intent

def test_detect_intent_empty_message():
    message = ""
    expected_intent = "Desconocido"
    assert detect_intent(message) == expected_intent