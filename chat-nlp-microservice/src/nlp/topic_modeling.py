from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import pandas as pd
import nltk
from nltk.corpus import stopwords
from typing import List, Dict

nltk.download('stopwords')

def preprocess_text(messages):
    stop_words = set(stopwords.words('spanish'))
    processed_messages = []
    
    for message in messages:
        words = message.split()
        filtered_words = [word for word in words if word.lower() not in stop_words]
        processed_messages.append(' '.join(filtered_words))
    
    return processed_messages

def extract_topics(messages: List[str], num_topics=3, num_words=5) -> List[str]:
    processed_messages = preprocess_text(messages)
    
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(processed_messages)
    
    lda = LatentDirichletAllocation(n_components=num_topics, random_state=42)
    lda.fit(tfidf_matrix)
    
    topics = []
    for idx, topic in enumerate(lda.components_):
        topic_words = [vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-num_words:]]
        topics.append(' '.join(topic_words))
    
    return topics

def get_frequent_topics(conversation):
    return extract_topics(conversation['messages'])