import os
from openai import OpenAI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str
    model: str = "gpt-3.5-turbo"

def ask_gpt(prompt, model="gpt-3.5-turbo"):
    """
    Send a prompt to OpenAI's API and return the response.
    
    Args:
        prompt: The text prompt to send to the API. e.g. "Hi there, you on the table. I wonder if you'd mind taking a brief survey? Five questions."
        model: The model to use (default: gpt-3.5-turbo)
        
    Returns:
        The text response from the API
    """
    # Get API key from environment variable
    api_key = os.environ.get("OPENAI_API_KEY")
    
    if not api_key:
        return "[ERROR: No API key found. Please set the OPENAI_API_KEY environment variable.]"
    
    # Map model names to actual OpenAI model identifiers
    model_map = {
        "gpt-3.5-turbo": "gpt-3.5-turbo",
        "o1-mini": "o1-mini"
    }
    
    # Use the mapped model name or the original if not in the map
    model_name = model_map.get(model, model)
    
    try:
        client = OpenAI(api_key=api_key)
        
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return f"[ERROR: {str(e)}]"

@app.post("/ask")
async def handle_ask(request: PromptRequest):
    response = ask_gpt(request.prompt, request.model)
    return {"response": response}

@app.get("/")
async def home():
    return {"message": "OpenAI API Service is running. Use POST /ask to query."}

# For local testing and Render deployment
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)