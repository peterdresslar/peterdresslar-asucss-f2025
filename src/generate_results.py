"""
Generate pre-computed results for the Rule 110 AI experiment.
This script calls the OpenAI API and saves the responses to files,
so they can be included in the notebook without requiring API keys.
"""

import json
import os
import numpy as np
from src.idea_stub import ask_gpt

rule110_codex = {
    (0, 0, 0): 0,
    (0, 0, 1): 1,
    (0, 1, 0): 1,
    (0, 1, 1): 0,
    (1, 0, 0): 1,
    (1, 0, 1): 1,
    (1, 1, 0): 1,
    (1, 1, 1): 0,
}
def rule110(neighborhood):
    """Compute the next state of the Rule 110 cellular automaton."""
    return rule110_codex[neighborhood]

def run_rule110(initial_state, steps):
    """Compute the next state of the Rule 110 cellular automaton.

    Args:
        initial_state: list of 0s and 1s
        steps: number of steps to run

    Returns:
        list of states, each a list of 0s and 1s: including the initial state

    Note:
        With rule 110, the we know that the neighborhood has 3 cells and thus 8 (2^3) possible configurations.
        In fact, the name rule 110 when collapsed to binary is 01101110, which gives us a zero-indexed"codex" to match a 
        specific neighborhood pattern to a specific ruling. This means that with any state array of 0s and 1s, we can do some
        clever things with binary arithmetic to compute the next state.
        https://mathworld.wolfram.com/Rule110.html
    """
    # validate initial state and throw error if it contains anything other than 0s and 1s
    if initial_state is None or not isinstance(initial_state, list):
        raise ValueError("Initial state must be a non-empty list")
    if any(x not in [0, 1] for x in initial_state):
        raise ValueError("Initial state must contain only 0s and 1s")

    states = [initial_state]
    for _ in range(steps):
        previous_state = states[-1]
        new_state = []
        for i, cell in enumerate(previous_state):
            left_neighbor = previous_state[i-1] if i > 0 else 0
            right_neighbor = previous_state[i+1] if i < len(previous_state) - 1 else 0
            neighborhood = (left_neighbor, cell, right_neighbor)
            new_state.append(rule110[neighborhood])
            
        states.append(initial_state)
    return states

def generate_correct_results():
    """Generate the correct Rule 110 results and save to a file."""
    # Create initial state: fifteen 0s followed by a 1
    initial_state = [0] * 15 + [1]
    
    # Compute 10 steps
    states = run_rule110(initial_state, 10)
    
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