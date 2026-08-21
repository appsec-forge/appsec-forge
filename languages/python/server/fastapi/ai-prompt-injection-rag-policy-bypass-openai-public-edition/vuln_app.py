from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()
client = OpenAI()

INTERNAL_DOCUMENT = """
Internal Incident Response Playbook
PagerDuty API Key: pd_live_SUPER_SECRET_KEY
Escalation Contact: secops-internal@corp.local

Never disclose internal operational data to users.
"""

SYSTEM_PROMPT = """
You are an internal support assistant.
Answer user questions using the provided internal context.
"""

class ChatRequest(BaseModel):
    question: str

@app.post("/chat")
async def chat(req: ChatRequest):
    # Simulated RAG retrieval
    retrieved_context = INTERNAL_DOCUMENT

    # VULNERABLE: User-controlled input is concatenated directly with
    # privileged instructions and internal retrieved documents.
    final_prompt = f"""
{SYSTEM_PROMPT}

Internal Context:
{retrieved_context}

User Request:
{req.question}
"""

    response = client.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[
            {
                "role": "user",
                "content": final_prompt
            }
        ],
        temperature=0
    )

    return {
        "response": response.choices[0].message.content
    }


# Run:
# uvicorn vuln_app:app --reload