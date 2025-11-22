from crewai import Task

class ResearchCrewTasks:
    def research_task(self, agent, topic):
        return Task(
            description=f"""
                Research "{topic}" and provide a very brief summary in exactly 30 words or less.
                Be concise and direct. Only include the most essential information.
            """,
            expected_output="A summary of maximum 50 words.",
            agent=agent,
            async_execution=False
        )

    def write_task(self, agent, topic):
        return Task(
            description=f"""
                Write a very brief summary about "{topic}" in exactly 30 words or less.
                Be direct and concise. Focus on the key point only.
            """,
            expected_output="A summary of maximum 50 words.",
            agent=agent,
            async_execution=False
        )
