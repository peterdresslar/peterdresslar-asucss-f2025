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
    I study the universal constraints that govern complex systems—from biological regulation to social dynamics. 
    My work focuses on bridging the gap between abstract theory and reproducible science, using Large Language Models 
    to accelerate how we identify universal principles. I am equally passionate about the "how" of research, building 
    software tools and engineering practices that make scientific investigation more transparent and accessible.
    
"""
)

st.markdown("### Current Projects")

projects = [
    {
        "title": "HPA-Axis-Simulator",
        "description": "Browser-friendly simulator of hypothalamic–pituitary–adrenal axis dynamics and stress reactivity for educational use. Based on work by the Uri Alon Lab at Weizmann Institute of Science. [Try simulator](https://hpamodel-sim-fast-slow.streamlit.app/)",
    },
    {
        "title": "1-Dimensional Game of Life",
        "description": "Minimalist cellular automaton exploring 1D Life rules as a teaching aid for emergence. [View app](https://game-of-life-1d.streamlit.app/)",
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
