from typing import List, Dict
from dotenv import load_dotenv
import openai
import os


load_dotenv()
apenai.api_key = os.getenv("OPENAI_API_KEY")


def optimize_token_usage(messages: List[str]) -> List[str]:
    unique_messages = list(dict.fromkeys(messages))
    return unique_messages

def generate_summary(conversation_id: str, messages: List[str]) -> Dict:
    optimized_messages = optimize_token_usage(messages)
    conversation_text = " ".join(optimized_messages)
    prompt = (
        "Te voy a proporcionar una conversación donde una persona busca ayuda. "
        "Tu tarea es responder de manera cálida, empática y amigable, asegurándote de transmitir cercanía y apoyo. "
        "Evita sonar robótico o demasiado formal. Imagina que eres un asistente realmente interesado en ayudar.\n\n"
        "Aquí está la conversación:\n"
        f"{conversation_text}\n\n"
        "Responde de manera natural y servicial, como si estuvieras hablando con alguien que necesita orientación. "
        "Por ejemplo, podrías decir algo como:\n"
        "'¡Hola! 😊 Entiendo lo frustrante que esto puede ser, pero no te preocupes, estoy aquí para ayudarte. "
        "Cuéntame un poco más sobre lo que sucede y juntos encontraremos una solución.'\n\n"
        "Recuerda mantener un tono humano, cálido y cercano en tu respuesta."
    )
    response = openai.Chatcompletions.create(
        model="gpt-4",
        prompt=prompt,
        max_tokens=100
    )
    summary = response.choices[0].text.strip()
    
    return {
        "conversation_id": conversation_id,
        "summary": summary
    }