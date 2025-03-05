# Chat NLP Microservice

This project is a microservice designed to process live chat conversations using Natural Language Processing (NLP) techniques. It analyzes sentiment, detects user intentions, identifies key topics, and generates optimized summaries using GPT-4.

## Project Structure

```
chat-nlp-microservice
├── src
│   ├── main.py                  # Entry point of the microservice
│   ├── nlp
│   │   ├── sentiment_analysis.py # Functions for sentiment analysis
│   │   ├── intent_detection.py   # Functions for intent detection
│   │   ├── topic_modeling.py     # Functions for topic modeling
│   │   └── summarization.py      # Functions for summarization
│   ├── models
│   │   └── intent_model.pkl      # Pre-trained intent classification model
│   ├── utils
│   │   └── token_optimization.py  # Utility functions for token optimization
│   ├── tests
│   │   ├── test_sentiment_analysis.py # Unit tests for sentiment analysis
│   │   ├── test_intent_detection.py   # Unit tests for intent detection
│   │   ├── test_topic_modeling.py     # Unit tests for topic modeling
│   │   └── test_summarization.py      # Unit tests for summarization
├── Dockerfile                     # Docker configuration for the microservice
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
└── .env                           # Environment variables
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone https://github.com/igorariza/Ia-Conversations.git
   cd chat-nlp-microservice
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory and add necessary configuration settings and API keys.
   EXAMPLE:
   ```
   OPENAI_API_KEY= <API_KEY>
   REDIS_URL=redis://localhost:6379
   GPT_MODEL=gpt-4
   TOKEN_LIMIT=4096
   DEBUG=True
   ```

## Usage

## Docker recommended

To build and run the Docker container, use the following commands:

```
colima start 
docker build -t chat-nlp-microservice .
docker run -p 8000:8000 chat-nlp-microservice
```

## Local

To run the microservice, execute the following command:

```
# Add these lines to your ~/.zshrc

export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

# Reload the shell configuration
source ~/.zshrc

# Activate the virtual environment
pyenv activate myenv


python src/main.py
```
```
uvicorn src.main:app --reload
```

The service will start and listen for incoming requests.

## API Endpoints

- **POST /process_conversation/**: Analyzes a chat conversation for sentiment, intent, topics, and generates a summary.
  - **Request Body**: JSON containing the conversation history.
  ````
   {
    "conversation_id": "",
    "messages": [
        {
            "role": "user",
            "text": "Hola, cuentame un chiste",
            "timestamp": "2025-02-19T10:00:00Z"
        }
    ]
   }
  ````
  - **Response**: JSON with analysis results.
   ````
    {
      "conversation_id": "",
      "sentiment": "positive",
      "intent": "joke",
      "topics": ["jokes"],
      "summary": "Here is a joke: Why did the scarecrow win an award? Because he was outstanding in his field!"
    }
   ````

## Testing

To run the unit tests, use the following command:

```
pytest src/tests
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.