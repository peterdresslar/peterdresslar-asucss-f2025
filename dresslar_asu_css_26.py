# ASU CSS Personal Research Interests
# Author: Peter Dresslar

import streamlit as st

st.set_page_config(
    page_title="Peter Dresslar — ASU Research Interests",
    page_icon="📚",
)

# --- Sidebar: Bio & Contact
st.sidebar.title("Peter Dresslar")
st.sidebar.markdown("🌴 Honolulu, Hawaiʻi")

st.sidebar.markdown("### Bio")
st.sidebar.markdown(
    """
- MS Candidate in Complex Systems Science at Arizona State University. (expected graduation: summer 2026)
- Program Manager for Technology Modernization at American Samoa Community College.
- Maintainer of [Zotero MCP](https://github.com/54yyyu/zotero-mcp) — connects Zotero research libraries with AI assistants via Model Context Protocol.

Interests: LLMs & alignment, agent-based models, computational social science, 
biologically inspired computation, and research tooling.
"""
)

st.sidebar.markdown("### Contact")
st.sidebar.markdown(
    """
- **Email:** pdressla@asu.edu
- **GitHub:** https://github.com/peterdresslar
- **LinkedIn:** https://www.linkedin.com/in/peter-dresslar/
- **ORCiD:** https://orcid.org/0000-0002-3893-4103
- **Medium:** https://medium.com/@peterdresslar
"""
)

# --- Main Content
st.title("Research Interests")

st.markdown(
    """
I study the causal roots of complex phenomena and the mathematical formalisms that describe them. Of particular interest to me is
 the degree to which large language models can change and possibly accelerate our pursuit of identifying 
universal principles across systems—from biological regulation to social dynamics. I am also a fan of software engineering practices and tools
that make scientific investigation more accessible and reproducible.
"""
)

st.markdown("### Current Projects")

projects = [
    {
        "title": "Do Android Wolves Dream of Artificial Sheep",
        "description": "LLM-driven agents in simulated ecologies using predator–prey metaphors to study cooperation, deception, and resource dynamics.",
    },
    {
        "title": "HPA-Axis-Simulator",
        "description": "With Alon Lab. Browser-friendly simulator of hypothalamic–pituitary–adrenal axis dynamics and stress reactivity for educational use. [Try simulator](https://hpamodel-sim-fast-slow.streamlit.app/)",
    },
    {
        "title": "Easy Evolvability",
        "description": "Just an idea. for now.",
    },
    {
        "title": "ASU RSE Streamlit Hosting Service",
        "description": "Conceptualizing internal Streamlit hosting at ASU focused on simplicity, governance, and researcher experience. [View service](https://app-dot-asu-dot-edu.streamlit.app/)",
    },
    {
        "title": "1-Dimensional Game of Life",
        "description": "Minimalist cellular automaton exploring 1D Life rules as a teaching aid for emergence.",
    },
    {
        "title": "Cognitive Bias in LLMs for ABM",
        "description": "Investigating LLM cognitive biases as controllable parameters in agent-based models of human systems.",
    },
]

for project in projects:
    st.markdown(f"**{project['title']}**")
    st.markdown(project['description'])
    st.markdown("")
