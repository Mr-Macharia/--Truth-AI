import streamlit as st
import os
from dotenv import load_dotenv
from crewai import Crew, Process
from src.agents import ResearchCrewAgents
from src.tasks import ResearchCrewTasks
from src.memory import AgentMemory

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Fact or Myth Agent",
    page_icon="🔍",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .result-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .stButton>button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'memory' not in st.session_state:
    st.session_state.memory = AgentMemory()
if 'history' not in st.session_state:
    st.session_state.history = []
if 'last_result' not in st.session_state:
    st.session_state.last_result = None

# Header
st.markdown('<div class="main-header">🔍 AI Fact or Myth Agent</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Verify facts and debunk myths with AI-powered research</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("ℹ️ About")
    st.write("""
    This AI agent helps you verify facts and debunk myths using:
    - **Perplexity AI** for web research
    - **Google Gemini** for analysis
    - **CrewAI** for orchestration
    """)
    
    st.header("📊 Session Stats")
    st.metric("Questions Asked", len(st.session_state.history))
    
    if st.button("🗑️ Clear History"):
        st.session_state.history = []
        st.session_state.memory = AgentMemory()
        st.rerun()
    
    st.header("💡 Example Questions")
    examples = [
        "Is coffee bad for your health?",
        "Did humans land on the moon?",
        "Is climate change real?",
        "Can AI replace human jobs?"
    ]
    for example in examples:
        if st.button(example, key=example):
            st.session_state.current_question = example

# Main input area
st.markdown("### Ask Your Question")

# Display conversation history at the top for context
if st.session_state.history:
    st.markdown("#### 💬 Current Conversation")
    for item in st.session_state.history[-3:]:  # Show last 3 exchanges
        st.markdown(f"**You:** {item['question']}")
        st.markdown(f"**AI:** {item['answer']}")
        st.markdown("---")

# Use chat input for better UX
question = st.chat_input("Continue the conversation or ask a new question...")

# Add control buttons in sidebar
with st.sidebar:
    st.markdown("---")
    if st.button("🆕 New Topic", use_container_width=True):
        st.session_state.history = []
        st.session_state.memory = AgentMemory()
        st.session_state.last_result = None
        st.rerun()

# Process question
if question:
    with st.spinner("🤖 Researching and analyzing..."):
        try:
            # Retrieve relevant memories for context
            past_context = st.session_state.memory.get_memories(question)
            
            # Inject memory context if relevant
            if past_context and past_context != "No relevant memories found.":
                enhanced_topic = f"{question}\n\nPrevious context: {past_context}"
            else:
                enhanced_topic = question

            # Create agents and tasks
            agents = ResearchCrewAgents()
            tasks = ResearchCrewTasks()
            
            researcher_agent = agents.researcher()
            research_task = tasks.research_task(researcher_agent, enhanced_topic)
            
            # Create and run crew
            crew = Crew(
                agents=[researcher_agent],
                tasks=[research_task],
                verbose=False,  # Set to False for cleaner Streamlit output
                process=Process.sequential
            )
            
            result = crew.kickoff()
            
            # Store in memory and history
            st.session_state.memory.add_memory(f"Question: {question}\nAnswer: {result}")
            st.session_state.history.append({
                'question': question,
                'answer': str(result)
            })
            st.session_state.last_result = str(result)
            
            # Display result
            st.success("✅ Fact Checked!")
            st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
            st.info("Please check your API keys and try again.")

# Display full conversation history in expandable section
if len(st.session_state.history) > 3:
    st.markdown("---")
    with st.expander(f"📜 Full Conversation History ({len(st.session_state.history)} questions)"):
        for i, item in enumerate(st.session_state.history, 1):
            st.markdown(f"**{i}. Q:** {item['question']}")
            st.markdown(f"**A:** {item['answer']}")
            st.markdown("---")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>"
    "Powered by CrewAI, Google Gemini & Perplexity AI"
    "</div>",
    unsafe_allow_html=True
)
