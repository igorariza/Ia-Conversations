from textblob import TextBlob

def analyze_sentiment(messages):
    sentiment_results = []
    total_sentiment = 0
    negative_messages = []

    for message in messages:
        analysis = TextBlob(message['text'])
        sentiment_score = analysis.sentiment.polarity
        sentiment = "neutral"

        if sentiment_score > 0:
            sentiment = "positive"
        elif sentiment_score < 0:
            sentiment = "negative"
            negative_messages.append(message['text'])

        sentiment_results.append({
            "message": message['text'],
            "sentiment": sentiment,
            "score": sentiment_score
        })
        total_sentiment += sentiment_score

    average_sentiment = "neutral"
    if total_sentiment > 0:
        average_sentiment = "positive"
    elif total_sentiment < 0:
        average_sentiment = "negative"

    return {
        "sentiment_analysis": sentiment_results,
        "average_sentiment": average_sentiment,
        "high_negative_messages": negative_messages
    }