# 🚀 MCP BDD Generator using Groq (LLaMA3 or Mixtral)

This FastAPI server fetches user stories (mock or Jira-based), sends them to a Groq LLM (like `llama3-70b-8192`), and converts them into Gherkin-style BDD test cases.

Each output is saved as a `.feature` file under the `bdd_output/` folder.

---

## 🧰 Requirements

- Python 3.10+
- [Groq API Key](https://console.groq.com/)
- pip or [uv](https://github.com/astral-sh/uv)
- (Optional) Jira API credentials

---

## 📦 Setup Instructions

### 1. Clone or Download the Project

```bash
git clone https://github.com/yatin-sammal/MCP-Server-For-Test-Cases-Generation
cd mcp_azure_bdd
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
# Groq
GROQ_API_KEY=your-groq-api-key
GROQ_MODEL=llama3-70b-8192  # or mixtral-8x7b-32768

# Jira (optional)
JIRA_BASE_URL=https://your-domain.atlassian.net
JIRA_PROJECT_KEY=YOURPROJECT
JIRA_EMAIL=you@example.com
JIRA_API_TOKEN=your-jira-api-token
```

> ✅ The Jira integration is optional — you can start with mock data using `/test-bdd`.

---

## 🚀 Run the Server

```bash
uvicorn main:app --reload
```

---

## 🧪 Endpoints

### `GET /test-bdd`

Generates BDD test cases from hardcoded user stories and saves them as `.feature` files.
You can check out the generated test cases and feature files for the hardcoded user stories in the bdd_output folder.

### `GET /generate-bdd`

Fetches user stories from Jira (if configured), converts them to BDDs using Groq, and saves them as `.feature` files.

---

## 📂 Output

Generated files are saved in the `bdd_output/` folder like:

```gherkin
Feature: Password reset

  Scenario: User resets password via email
    Given a user has forgotten their password
    When they request a password reset
    Then they receive a link via email
```

---

## 🧠 Models Supported (Groq)

You can use:
- `llama3-70b-8192`
- `mixtral-8x7b-32768`
- `gemma-7b-it`

Update your `.env` file with the model you prefer.

---

## 🛠 Troubleshooting

- **Missing `GROQ_API_KEY`**: Ensure `.env` is loaded or use `source .env`
- **500 Internal Server Error**: Check terminal logs for missing credentials or invalid responses
- **Permission issues**: Make sure `bdd_output/` is writeable

---

## 📌 License

MIT
