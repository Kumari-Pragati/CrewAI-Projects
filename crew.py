from crewai import Crew, Process
from MyAgents import blog_researcher, blog_writer

# Dynamic topic
topic = "AI in Healthcare"

# Dynamically build tasks
from crewai import Task

researcher_task = Task(
    description=f"Research the latest trends and developments in {topic}.",
    expected_output="A well-structured summary with references.",
    agent=blog_researcher
)

writer_task = Task(
    description=f"Write a compelling blog article based on research about {topic}.",
    expected_output="A full-length blog post ready to publish.",
    agent=blog_writer
)

# Forming the Crew
crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[researcher_task, writer_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

# Running the Crew
result = crew.kickoff()  # ✅ No input param needed
print(result)
# The result will contain the output of the tasks performed by the agents in the crew.
# The output will be a dictionary with the task names as keys and the task outputs as values.