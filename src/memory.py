import os
from dotenv import load_dotenv

load_dotenv()

class AgentMemory:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AgentMemory, cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        # Simple in-memory conversation history
        self.conversation_history = []
        print(f"Memory system initialized (in-memory storage)")

    def add_memory(self, content, user_id="default_user"):
        """
        Store memory in conversation history.
        """
        try:
            self.conversation_history.append(content)
            # Keep only last 10 conversations to avoid context overflow
            if len(self.conversation_history) > 10:
                self.conversation_history = self.conversation_history[-10:]
            return True
        except Exception as e:
            print(f"Error adding memory: {e}")
            return False

    def get_memories(self, query, user_id="default_user"):
        """
        Retrieve recent memories from conversation history.
        """
        try:
            if not self.conversation_history:
                return "No relevant memories found."
            
            # Return last 3 conversations for context
            recent_memories = self.conversation_history[-3:]
            return "\n\n".join(recent_memories)
        except Exception as e:
            print(f"Error retrieving memories: {e}")
            return "No relevant memories found."
