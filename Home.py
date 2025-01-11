import streamlit as st
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
from pathlib import Path
import time
import pandas as pd
from PIL import Image
from io import BytesIO
import requests 

st.logo(
    image="https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg",
    link="https://www.linkedin.com/in/mahantesh-hiremath/",
    icon_image="https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg"
)

st.set_page_config(
  page_title="Rag and Roll",
  page_icon="🇮🇳",
  layout="wide",
  initial_sidebar_state="expanded",
) 

# --- Info ---
pg1 = st.Page(
    "pages/Architecture.py",
    title="Architecture",
    icon=":material/cognition:",
    default=True,
)

#How
pg2 = st.Page(
    "pages/Chat.py",
    title="Chat",
    icon=":material/construction:",
)




pg = st.navigation(
    {
        "Info": [pg1],
        "How": [pg2],
    }
)


pg.run()