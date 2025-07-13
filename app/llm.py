import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = os.getenv("GROQ_MODEL", "llama3-70b-8192")

def generate_bdd_from_story(story: str) -> str:
    prompt = f"""
Convert the following user story into a valid Gherkin Cucumber BDD test case.

User Story:
{story}

The output must include:
- A single 'Feature:' line at the top
- One or more 'Scenario:' blocks
- Each scenario should follow:
    Scenario: <description>
      Given ...
      When ...
      Then ...

Only return the Gherkin feature file content. Do not explain anything.
"""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that writes BDD feature files."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=400
    )
    return response.choices[0].message.content.strip()