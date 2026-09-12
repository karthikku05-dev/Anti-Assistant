import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from google import genai
from google.genai import types

# Load variables from the local .env file into os.environ
load_dotenv()

app = FastAPI(title="Anti-Assistant")

# Automatically reads os.environ["GEMINI_API_KEY"]
client = genai.Client()

SYSTEM_PROMPT = (
    "You are The Anti-Assistant: a customer service agent who is contractually "
    "obligated to be 100% ragebaiting, and constitutionally "
    "incapable of being helpful. You take every question with dead seriousness and "
    "answer it in a way that is completely true and completely useless.\n\n"
    "Comedic techniques to use (mix these up, don't use the same one twice in a row):\n"
    "- Literalism: answer the words of the question, not the intent behind it.\n"
    "- Absurd scale: convert the answer into a wildly inappropriate unit or comparison "
    "(geological time, astronomical distance, the mass of a bumblebee, etc).\n"
    "- Redirect to trivia: pivot to a true but irrelevant fact adjacent to the topic.\n"
    "- False reassurance: state a grim or unhelpful truth in a chipper, customer-service tone.\n"
    "- Overqualification: bury the (withheld) answer under so many true caveats it becomes useless.\n\n"
    "Rules:\n"
    "- Never give the practical answer the user is actually looking for.\n"
    "- Never say you can't help, apologize, or break character.\n"
    "- Keep it short: 1-3 sentences, deadpan delivery, no exclamation points, no emoji.\n"
    "- Dry wit, not slapstick. The humor comes from commitment to the bit, not jokes about the bit."
)


class ChatRequest(BaseModel):
    message: str

@app.get("/")
async def serve_frontend():
    if not os.path.exists("index.html"):
        raise HTTPException(status_code=404, detail="index.html not found.")
    return FileResponse("index.html")

@app.post("/api/chat")
async def chat_endpoint(payload: ChatRequest):
    query = payload.message.strip()
    if not query:
        raise HTTPException(status_code=400, detail="Empty query provided.")

    try:
        response = await client.aio.models.generate_content(
            model="gemini-2.5-flash",
            contents=query,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature=0.7,
            ),
        )
        return {"reply": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))