import requests
import os

def fetch_jira_stories():
    url = f"{os.getenv('JIRA_BASE_URL')}/rest/api/3/search"
    auth = (os.getenv('JIRA_EMAIL'), os.getenv('JIRA_API_TOKEN'))
    jql = {
        "jql": f"project={os.getenv('JIRA_PROJECT_KEY')} AND issuetype=Story AND status!=Done",
        "maxResults": 5
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=jql, auth=auth, headers=headers)
    data = response.json()
    return [issue['fields']['summary'] for issue in data.get("issues", [])]