from typing import List
import spacy


nlp = spacy.load("en_core_web_sm")

def detect_intent(messages: List[str]) -> List[str]:
    intents = []
    
    for message in messages:
        doc = nlp(message)
        if any(token.lemma_ in ["help", "assist", "support"] for token in doc):
            intents.append("Solicitud de soporte")
        elif any(token.lemma_ in ["complain", "issue", "problem"] for token in doc):
            intents.append("Queja")
        elif any(token.lemma_ in ["status", "check", "know"] for token in doc):
            intents.append("Consulta")
        else:
            intents.append("Otro")
    
    return intents

def get_common_intents(messages: List[str]) -> List[str]:
    detected_intents = detect_intent(messages)
    common_intents = list(set(detected_intents))
    return common_intents