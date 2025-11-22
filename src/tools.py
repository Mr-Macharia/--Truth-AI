import os
import requests
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from src.memory import AgentMemory

class PerplexitySearchInput(BaseModel):
    """Input schema for PerplexitySearchTool."""
    query: str = Field(..., description="The search query to send to Perplexity AI")

class PerplexitySearchTool(BaseTool):
    name: str = "Perplexity Search"
    description: str = "Useful to search the internet for information using Perplexity AI. Returns the answer and citations."
    args_schema: type[BaseModel] = PerplexitySearchInput

    def _run(self, query: str) -> str:
        url = "https://api.perplexity.ai/chat/completions"
        api_key = os.getenv("PERPLEXITY_API_KEY")
        model = os.getenv("PERPLEXITY_MODEL", "llama-3.1-sonar-large-128k-online")
        
        if not api_key:
            return "Error: PERPLEXITY_API_KEY not found in environment variables."

        payload = {
            "model": model,
            "messages": [
                {
                    "role": "system",
                    "content": "Be precise and concise."
                },
                {
                    "role": "user",
                    "content": query
                }
            ]
        }
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            result = response.json()
            return result['choices'][0]['message']['content']
        except Exception as e:
            return f"Error performing search: {e}"

class SaveMemoryInput(BaseModel):
    """Input schema for SaveMemoryTool."""
    content: str = Field(..., description="The content to save to memory")

class SaveMemoryTool(BaseTool):
    name: str = "Save Memory"
    description: str = "Useful to save important information, facts, or context for future reference."
    args_schema: type[BaseModel] = SaveMemoryInput

    def _run(self, content: str) -> str:
        memory = AgentMemory()
        memory.add_memory(content)
        return "Memory saved successfully."

class RecallMemoryInput(BaseModel):
    """Input schema for RecallMemoryTool."""
    query: str = Field(..., description="The query to search for in memories")

class RecallMemoryTool(BaseTool):
    name: str = "Recall Memory"
    description: str = "Useful to search for past memories, conversations, or facts related to a query."
    args_schema: type[BaseModel] = RecallMemoryInput

    def _run(self, query: str) -> str:
        memory = AgentMemory()
        results = memory.get_memories(query)
        return str(results)

class SearchTools:
    search_perplexity = PerplexitySearchTool()

class MemoryTools:
    save_memory = SaveMemoryTool()
    recall_memory = RecallMemoryTool()

