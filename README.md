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
   git clone <repository-url>
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

- **POST /analyze**: Analyzes a chat conversation for sentiment, intent, topics, and generates a summary.
  - **Request Body**: JSON containing the conversation history.
  - **Response**: JSON with analysis results.

## Testing

To run the unit tests, use the following command:

```
pytest src/tests
```

## Docker

To build and run the Docker container, use the following commands:

```
docker build -t chat-nlp-microservice .
docker run -p 8000:8000 chat-nlp-microservice
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.