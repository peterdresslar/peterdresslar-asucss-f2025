# Rule 110 AI Experiment

This repository contains a Jupyter notebook that demonstrates how AI models have evolved in their ability to emulate cellular automata, specifically Rule 110.

## Background

Rule 110 is a one-dimensional cellular automaton that has been proven to be Turing complete. This experiment tests how well different AI models (GPT-3.5 and GPT-4o mini) can "think through" the steps of Rule 110 computation.

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
4. Run the Jupyter notebook:
   ```
   jupyter notebook research-statement.ipynb
   ```

## Files

- `research-statement.ipynb`: The main notebook containing the experiment and analysis
- `main.py`: Helper functions for making API calls to OpenAI
- `requirements.txt`: Python dependencies
- `.env`: (You need to create this) Contains your OpenAI API key

## How It Works

The notebook:
1. Implements Rule 110 in Python for reference
2. Asks GPT-3.5 to compute Rule 110 steps
3. Asks GPT-4o mini to compute the same steps
4. Compares the AI outputs to the correct implementation
5. Analyzes the results

## Results

The experiment demonstrates how newer AI models (GPT-4o mini) are significantly better at emulating complex computational processes like Rule 110 compared to earlier models (GPT-3.5).

## Note

This is part of a personal statement for a Complex Systems Science degree application, demonstrating the intersection of AI and complex systems.

## Organization

```bash
.                 # Root
├── app/          # Streamlit app
├── docs/         # Grad school entrance application notebook, note code requires a running service.
└── src/          # The service code for the notebook, currently no longer deployed anywhere. Includes some unfinished ideas.
```
