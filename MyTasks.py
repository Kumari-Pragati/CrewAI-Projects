from crewai import Task
from MyTools import md_tool
from MyAgents import blog_researcher, blog_writer

#Researcher task 
# This is a custom task that can be used to perform to create blog's content as a blog researcher.
# The task will be created with the following parameters:
researcher_task = Task(
    description=(
        "Identify the topic of the blog post and provide a list of 10 blog post ideas related to that topic. "
        "You are a blog researcher. You will be given a topic {topic} and you will provide a list of 10 blog post ideas related to that topic."
    ),
    expected_output=
        "A list of 10 blog post ideas related to the topic {topic}.",
    tools=[md_tool],
    agent=blog_researcher,
)   

# Writer task
# This is a custom task that can be used to perform to create blog's content as a blog writer.
# The task will be created with the following parameters:
writer_task = Task(
    description=(
        "Write a blog post based on the topic {topic} and the list of blog post ideas provided by the researcher. "
        "You are a blog writer. You will be given a topic {topic} and you will write a blog post about that topic."
    ),
    expected_output=
        "A blog post about the topic {topic}.",
    tools=[md_tool],
    agent=blog_writer,
    async_execution=False,
    output_file="new_blog_post.md",
)