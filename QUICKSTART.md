# Quick Start Guide 🚀

Get up and running with the AI Fact or Myth Agent in 5 minutes!

## Step-by-Step Setup

### 1. Get Your API Keys

Before you begin, obtain these free API keys:

#### Google Gemini API Key
1. Go to [Google AI Studio](https://ai.google.dev/)
2. Click "Get API Key"
3. Sign in with your Google account
4. Create a new API key
5. Copy the key (starts with `AIza...`)

#### Perplexity API Key
1. Go to [Perplexity AI](https://www.perplexity.ai/)
2. Sign up for an account
3. Navigate to [API Settings](https://www.perplexity.ai/settings/api)
4. Generate a new API key
5. Copy the key (starts with `pplx-...`)

### 2. Install Python Environment

**Option A: Using Conda (Recommended)**
```bash
# Create environment
conda create -n app_env python=3.10

# Activate environment
conda activate app_env

# Install packages
pip install -r requirements.txt
```

**Option B: Using venv**
```bash
# Create environment
python -m venv app_env

# Activate environment (Windows)
app_env\Scripts\activate

# Activate environment (macOS/Linux)
source app_env/bin/activate

# Install packages
pip install -r requirements.txt
```

### 3. Configure API Keys

Create a file named `.env` in the project root directory:

```env
GEMINI_API_KEY=AIzaSy...your-actual-key-here
PERPLEXITY_API_KEY=pplx-...your-actual-key-here
PERPLEXITY_MODEL=sonar
```

**⚠️ Important**: 
- Replace the placeholder values with your actual API keys
- Never commit the `.env` file to version control
- Keep your API keys secret

### 4. Run the Agent

**Web Interface (Recommended):**
```bash
streamlit run app.py
```
Your browser will open to `http://localhost:8501`

**Command Line:**
```bash
python main.py
```

### 5. Start Asking Questions!

```
Welcome to the AI Fact or Myth Agent
---------------------------------------------
Type 'exit' to quit the program

Enter the information you want to confirm: 
```

Type any question or claim you want to verify, then press Enter.

## Example Questions

Try these to get started:

- `Is coffee bad for your health?`
- `Did humans land on the moon?`
- `Is cryptocurrency a safe investment?`
- `Can AI replace human jobs?`
- `Is climate change real?`

## Tips for Best Results

✅ **Do:**
- Ask specific, clear questions
- Use follow-up questions for more context
- Type `exit` when you're done

❌ **Don't:**
- Ask multiple unrelated questions at once
- Expect extremely long answers (responses are limited to 30 words)
- Leave the session idle for extended periods

## Common Commands

| Command | Action |
|---------|--------|
| Type your question | Get a fact-checked answer |
| Press Enter (empty) | Uses default example question |
| Type `exit` | Quit the program |

## Troubleshooting Quick Fixes

### "API key not found"
- Check your `.env` file exists
- Verify API keys are correct
- Ensure no extra spaces in `.env`

### "Module not found"
```bash
conda activate app_env
pip install -r requirements.txt
```

### "Rate limit exceeded"
- You've used up your free API quota
- Wait 24 hours or upgrade your API plan
- Try using fewer questions

## Next Steps

Once you're comfortable with basic usage:

1. Read the full [README.md](README.md) for advanced configuration
2. Explore the `src/` directory to understand the code
3. Customize response length in `src/tasks.py`
4. Try different AI models in `src/agents.py`

## Need Help?

- Check [README.md](README.md) for detailed documentation
- Open an issue on GitHub for bugs
- Review error messages carefully—they usually indicate the problem

---

**Ready to start? Run `python main.py` now! 🎉**
