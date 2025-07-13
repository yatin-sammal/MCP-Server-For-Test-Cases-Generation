from fastapi import APIRouter
from app.jira import fetch_jira_stories
from app.llm import generate_bdd_from_story
from app.bdd_writer import save_bdd_to_file
import os

router = APIRouter()

@router.get("/generate-bdd")
def generate_bdd():
    stories = fetch_jira_stories()
    output = []
    for story in stories:
        bdd = generate_bdd_from_story(story)
        filename = save_bdd_to_file(story, bdd)
        output.append({"story": story, "bdd": bdd, "file": filename})
    return output

@router.get("/test-bdd")
def test_bdd():
    stories = [
        "As a shopper, I want to add items to my cart so I can buy them later",
        "As a user, I want to receive email notifications when my order ships"
    ]
    output = []
    for story in stories:
        print(f"Generating BDD for: {story}")
        try:
            bdd = generate_bdd_from_story(story)
            print("LLM response:", bdd)
            filename = save_bdd_to_file(story, bdd)
            output.append({"story": story, "bdd": bdd, "file": filename})
        except Exception as e:
            print("Error during BDD generation:", e)
            output.append({"story": story, "error": str(e)})
    return output
