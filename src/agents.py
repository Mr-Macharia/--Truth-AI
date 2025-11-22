import os
from crewai import Agent, LLM
from src.tools import SearchTools, MemoryTools

class ResearchCrewAgents:
    def __init__(self):
        self.llm = LLM(
            model="gemini/gemini-2.5-flash",
            temperature=0.5,
            api_key=os.getenv("GEMINI_API_KEY")
        )

    def researcher(self):
        return Agent(
            role='Information Fact Checker',
            goal='Uncover whether the facts are real or misleading',
            backstory="""You are an expert fact checker with top-tier explanations.
            Your expertise lies in identifying whether the information presented is accurate or misleading.
            You have a knack for dissecting information and presenting confirmed and debunked facts.
            You always check your memory for past context before starting new research.""",
            verbose=True,
            allow_delegation=False,
            tools=[
                SearchTools.search_perplexity,
                MemoryTools.save_memory,
                MemoryTools.recall_memory
            ],
            llm=self.llm
        )

    def writer(self):
        return Agent(
            role='Information Corrector',
            goal='Explain the fact or misinformation clearly and accurately in a way that is easy to understand.',
            backstory="""You are an information corrector known for preventing misinformation and explaining correct information clearly.
            You have a knack for explaining information in a way that is easy to understand and accurate.
            You rely on the researcher's findings to produce high-quality articles.""",
            verbose=True,
            allow_delegation=True,
            tools=[
                MemoryTools.save_memory,
                MemoryTools.recall_memory
            ],
            llm=self.llm
        )
