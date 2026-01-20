# Peter Dresslar ASU Complex Systems Science 2025-2026

This repository contains some artifacts from my time in Arizona State University's Complex Systems Science master's degree program. There is a notebook that I submitted as part of my application (possibly not giving my candidacy a boost: but I was accepted nonetheless.) 

I also have a [Streamlit](https://streamlit.io) app that powers a compact web application and serves as a sort of "portfolio" as I progress through the program.

## Background on the Notebook

Rule 110 is a one-dimensional cellular automaton that has been proven to be Turing complete. The included "experiment" tests how well different AI models (GPT-3.5 and GPT-4o mini) can "think through" the steps of Rule 110 computation, in an attempt to tell a story. In retrospect this would have been a far better Streamlit app itself---perhaps this is an idea for a future enhancement.

## Setup for the notebook

1. Clone this repository

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory with your OpenAI API key:

   ```bash
   OPENAI_API_KEY=your_api_key_here
   ```
4. Run the Jupyter notebook:

   ```bash
   jupyter notebook research-statement.ipynb
   ```

The notebook:
1. Implements Rule 110 in Python for reference
2. Asks GPT-3.5 to compute Rule 110 steps
3. Asks GPT-4o mini to compute the same steps
4. Compares the AI outputs to the correct implementation
5. Analyzes the results

## Setup for the Streamlit app

It is so easy to run the Streamlit app with `uv`. Maybe try it! If you have `uv` installed, you can:

```sh
uv venv
source .venv/bin/activate  # on Windows, activating the venv looks more like .\.venv\Scripts\activate
uv sync
uv run streamlit run app/portfolio.py
```

If you do not have uv installed, and are interested in more information, see the docs, [here](https://docs.astral.sh/uv).

## The files in src/

This was the original service that I hosted for a while to support API calls to LLMs from my notebook. It worked quite nicely, but today I would probably take a different path. Consider the code in src/ to be work-in-progress (for some value of in-progress!)

## Organization

```bash
.                 # Root
├── app/          # Streamlit app
├── docs/         # Grad school entrance application notebook, note code requires a running service.
└── src/          # The service code for the notebook, currently no longer deployed anywhere. Includes some unfinished ideas.
```
