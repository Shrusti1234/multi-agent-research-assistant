from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# Writer chain
writer_prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human",
     """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report EXACTLY in Markdown format like this:

# Research Report: {topic}

## Introduction

## Key Findings
- Include at least 3 detailed findings.

## Conclusion

## Sources
- List all source URLs.

Be detailed, factual and professional.""")
])

writer_chain = writer_prompt | llm | StrOutputParser()

# Critic chain
critic_prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a sharp and constructive research critic."),
    ("human",
     """Review the research report below.

Report:
{report}

Respond in this exact format:

# Critic Review

## Score
X/10

## Strengths
- ...

## Areas to Improve
- ...

## One Line Verdict
...""")
])

critic_chain = critic_prompt | llm | StrOutputParser()