def optimize_token_usage(messages):
    optimized_messages = []
    seen_messages = set()

    for message in messages:
        # Remove redundant messages
        if message['text'] not in seen_messages:
            seen_messages.add(message['text'])
            optimized_messages.append(message)

    return optimized_messages

def prioritize_key_parts(messages):
    # This function can be expanded to prioritize messages based on certain criteria
    # For now, it simply returns the messages as is
    return messages

def prepare_for_gpt4(messages):
    optimized = optimize_token_usage(messages)
    prioritized = prioritize_key_parts(optimized)
    return prioritized