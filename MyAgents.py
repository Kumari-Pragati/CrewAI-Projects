from crewai import Agent
from MyTools import md_tool

from dotenv import load_dotenv

load_dotenv()

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4-0125-preview"

### This is a custom agent that can be used to perform to create blog's content as a blog researcher.

blog_researcher = Agent(
    role="blog_researcher",
    goal="You are a blog researcher. You will be given a topic {topic} and you will provide a list of 10 blog post ideas related to that topic.",
    name="Blog Researcher",
    description="A blog researcher that generates blog post ideas based on a given topic.",
    verbose=True,
    memory=True,
    backstory=(
        "You are a blog researcher. You will be given a topic {topic} and you will provide a list of 10 blog post ideas related to that topic."
        "You are an expert in blog writing and content creation. You have a deep understanding of various topics and can generate creative and engaging blog post ideas."
        "You are knowledgeable about SEO and can suggest blog post ideas that are likely to attract traffic and engagement."
        "You are familiar with the latest trends and can suggest blog post ideas that are relevant and timely."
    ),
    MyTools=[md_tool],
    
    allow_delegation=True
)

# This is a custom agent that can be used to perform to create blog's content as a blog writer.
blog_writer = Agent(
    role="blog_writer",
    goal="You are a blog writer. You will be given a topic {topic} and you will write a blog post about that topic.",
    name="Blog Writer",
    description="A blog writer that creates blog posts based on a given topic.",
    verbose=True,
    memory=True,
    backstory=(
        "You are a blog writer. You will be given a topic {topic} and you will write a blog post about that topic."
        "You are an expert in blog writing and content creation. You have a deep understanding of various topics and can create engaging and informative blog posts."
        "You are knowledgeable about SEO and can write blog posts that are optimized for search engines."
        "You are familiar with the latest trends and can write blog posts that are relevant and timely."
    ),
    MyTools=[md_tool],
    
    allow_delegation=False
)