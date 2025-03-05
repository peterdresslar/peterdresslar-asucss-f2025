"""
Generate pre-computed results for the Rule 110 AI experiment.
This script calls the OpenAI API and saves the responses to files,
so they can be included in the notebook without requiring API keys.
"""

import json
import os
from main import ask_gpt
from rule110 import rule110

def generate_correct_results():
    """Generate the correct Rule 110 results and save to a file."""
    # Create initial state: fifteen 0s followed by a 1
    initial_state = [0] * 15 + [1]
    
    # Compute 10 steps
    states = rule110(initial_state, 10)
    
    # Convert to strings for easier display
    string_states = []
    for state in states:
        string_states.append(''.join(map(str, state)))
    
    # Save to file
    with open('correct_results.json', 'w') as f:
        json.dump(string_states, f, indent=2)
    
    print("Correct results saved to correct_results.json")

def generate_ai_results():
    """Generate AI model results and save to files."""
    prompt = """
Please output the first 10 values of Rule 110,
Given a 16 cell cylinder,
with the initial condition of 
fifteen 0s followed by a 1 (left to right).

Please work through the steps yourself. As a reminder, the rules of Rule 110 are:

Pattern | Next State
--------|----------
111 | 0
110 | 1
101 | 1
100 | 0
011 | 1
010 | 1
001 | 1
000 | 0

Kindly respond only with the output values, no other text. Thanks!
"""
    
    # Get GPT-3.5 response
    gpt35_response = ask_gpt(prompt, "gpt-3.5-turbo")
    with open('gpt35_results.txt', 'w') as f:
        f.write(gpt35_response)
    print("GPT-3.5 results saved to gpt35_results.txt")
    
    # Get GPT-4o mini response
    gpt4o_mini_response = ask_gpt(prompt, "o1-mini")
    with open('gpt4o_mini_results.txt', 'w') as f:
        f.write(gpt4o_mini_response)
    print("GPT-4o mini results saved to gpt4o_mini_results.txt")

if __name__ == "__main__":
    # Check if API key is set
    if not os.environ.get("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable not set.")
        print("Please set it before running this script.")
        exit(1)
    
    generate_correct_results()
    generate_ai_results()
    print("All results generated successfully!") 