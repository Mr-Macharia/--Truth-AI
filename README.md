# AI Fact or Myth Agent 

An intelligent AI agent that helps you verify facts and debunk myths using advanced research capabilities powered by CrewAI, Google Gemini, and Perplexity AI.

## Features

- **Real-time Web Research**: Uses Perplexity AI to search and verify information from the web
- **Intelligent Fact Checking**: Powered by Google Gemini 2.5 Flash for accurate analysis
- **Conversation Memory**: Remembers previous questions and answers for contextual follow-ups
- **Concise Responses**: Provides clear, 30-word summaries of complex information
- **Interactive Web UI**: Beautiful Streamlit interface for easy fact-checking
- **CLI Support**: Also available as a command-line interface

## Tech Stack

- **CrewAI**: Multi-agent orchestration framework
- **Google Gemini 2.5 Flash**: Large language model for analysis
- **Perplexity AI**: Web search and information retrieval
- **Python 3.x**: Core programming language

## Prerequisites

- Python 3.8 or higher
- Conda (recommended) or pip
- API Keys:
  - Google Gemini API key ([Get it here](https://ai.google.dev/))
  - Perplexity API key ([Get it here](https://www.perplexity.ai/))

## Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd "AI Tool Agent"
```

### 2. Create a Virtual Environment

**Using Conda (Recommended):**
```bash
conda create -n app_env python=3.10
conda activate app_env
```

**Using venv:**
```bash
python -m venv app_env
# On Windows:
app_env\Scripts\activate
# On macOS/Linux:
source app_env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory:

```bash
GEMINI_API_KEY=your-gemini-api-key-here
PERPLEXITY_API_KEY=your-perplexity-api-key-here
PERPLEXITY_MODEL=sonar
```

**Important**: Replace the placeholder values with your actual API keys.

## Usage

### Running the Streamlit Web App (Recommended)

```bash
streamlit run app.py
```

This will open the app in your default web browser at `http://localhost:8501`

**Features:**
- Clean, intuitive web interface
- Conversation history display
- Example questions in sidebar
- Session statistics
- One-click history clearing

### Running the CLI Version

```bash
python main.py
```

### Example Session

```
Welcome to the AI Fact or Myth Agent
---------------------------------------------
Type 'exit' to quit the program

Enter the information you want to confirm: Is the Earth flat?

[Agent processes the question...]

-------------------------
Here is your answer
---------------------------

Earth is spherical, not flat. This is confirmed by satellite images, gravity, 
time zones, and centuries of scientific evidence. Flat Earth claims are 
scientifically disproven.

Enter the information you want to confirm: Why do some people believe it?

[Agent remembers previous context about flat Earth...]

-------------------------
Here is your answer
---------------------------

People believe in flat Earth due to mistrust in institutions, social media 
misinformation, cognitive biases, and community reinforcement, despite 
overwhelming scientific evidence against it.

Enter the information you want to confirm: exit

Goodbye!
```

## Project Structure

```
AI Tool Agent/
├── src/
│   ├── agents.py          # AI agent definitions
│   ├── tasks.py           # Task definitions
│   ├── tools.py           # Custom tools (Perplexity search, memory)
│   └── memory.py          # Conversation memory management
├── app.py                 # Streamlit web application
├── main.py                # CLI application entry point
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not committed)
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## How It Works

1. **User Input**: You ask a question about any fact or claim
2. **Memory Check**: The agent checks previous conversations for context
3. **Web Research**: Perplexity AI searches the web for current information
4. **Analysis**: Google Gemini analyzes the information and forms conclusions
5. **Response**: You receive a concise, factual answer (30 words max)
6. **Memory Storage**: The conversation is saved for future context

## Configuration

### Adjusting Response Length

Edit `src/tasks.py` to change the word limit:

```python
description="""Research "{topic}" and provide a very brief summary in exactly 50 words or less."""
```

### Changing the AI Model

Edit `src/agents.py` to use a different Gemini model:

```python
self.llm = LLM(
    model="gemini/gemini-1.5-pro",  # Change model here
    temperature=0.5,
    api_key=os.getenv("GEMINI_API_KEY")
)
```

## Troubleshooting

### API Key Errors

**Problem**: `Error: API key not found`

**Solution**: Make sure your `.env` file exists and contains valid API keys.

### Import Errors

**Problem**: `ModuleNotFoundError: No module named 'crewai'`

**Solution**: Ensure you've activated your virtual environment and installed dependencies:
```bash
conda activate app_env  # or source app_env/bin/activate
pip install -r requirements.txt
```

### Model Quota Exceeded

**Problem**: `Error 429: Resource exhausted`

**Solution**: You've exceeded your API quota. Wait or upgrade your API plan.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## Acknowledgments

- **CrewAI** for the multi-agent framework
- **Google** for the Gemini API
- **Perplexity AI** for web search capabilities

## Contact

For questions or support, reach out on my email or linkedin.

---

**You're welcome**
