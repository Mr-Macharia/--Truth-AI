import os
from dotenv import load_dotenv
from crewai import Crew, Process
from src.agents import ResearchCrewAgents
from src.tasks import ResearchCrewTasks
from src.memory import AgentMemory

# Load environment variables
load_dotenv()

def run():
    print("Welcome to the AI Fact or Myth Agent")
    print("---------------------------------------------")
    print("Type 'exit' to quit the program\n")
    
    # Initialize Memory
    memory = AgentMemory()
    
    while True:
        topic = input("\nEnter the information you want to confirm: ")
        
        # Check for exit command
        if topic.lower() == 'exit':
            print("\nGoodbye!")
            break
        
        if not topic:
            topic = "AI Robots can have emotions"
            print(f"No topic provided. Using default: {topic}")

        # Retrieve relevant memories for context
        past_context = memory.get_memories(topic)
        
        # Inject memory context into topic if relevant memories exist
        if past_context and past_context != "No relevant memories found.":
            enhanced_topic = f"{topic}\n\nPrevious context: {past_context}"
        else:
            enhanced_topic = topic

        agents = ResearchCrewAgents()
        tasks = ResearchCrewTasks()

        # Create Agents
        researcher_agent = agents.researcher()

        # Create Tasks
        research_task = tasks.research_task(researcher_agent, enhanced_topic)

        # Create Crew
        crew = Crew(
            agents=[researcher_agent],
            tasks=[research_task],
            verbose=True,
            process=Process.sequential
        )

        result = crew.kickoff()

        print("\n\n-------------------------")
        print("Here is your answer")
        print("---------------------------\n")
        print(result)
        
        # Store the interaction in memory
        memory.add_memory(f"Question: {topic}\nAnswer: {result}")

if __name__ == "__main__":
    run()
