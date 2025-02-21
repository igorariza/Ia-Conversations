from typing import List, Dict
import openai

def optimize_token_usage(messages: List[str]) -> List[str]:
    # Remove redundant messages and prioritize key parts
    unique_messages = list(dict.fromkeys(messages))  # Preserve order and remove duplicates
    return unique_messages

def generate_summary(conversation_id: str, messages: List[str], api_key: str) -> Dict:
    optimized_messages = optimize_token_usage(messages)
    prompt = f"Summarize the following conversation:\n{optimized_messages}"
    
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150  # Adjust based on desired summary length
    )
    
    summary = response.choices[0].message['content']
    
    return {
        "conversation_id": conversation_id,
        "summary": summary
    }