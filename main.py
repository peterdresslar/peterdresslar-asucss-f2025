import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def ask_gpt(prompt, model="gpt-3.5-turbo"):
    """
    Send a prompt to OpenAI's API and return the response.
    
    Args:
        prompt: The text prompt to send to the API
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
        "o1-mini": "gpt-4o-mini"
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

# For testing purposes
if __name__ == "__main__":
    # Example usage
    test_prompt = "Say hello world"
    print(ask_gpt(test_prompt))
