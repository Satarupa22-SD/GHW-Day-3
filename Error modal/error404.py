import streamlit as st
import streamlit_lottie as st_lottie
from streamlit_lottie import st_lottie
import requests


st.set_page_config(page_title="ERROR 404", page_icon=":broken_heart:",layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

coding_error = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_suhe7qtm.json")

with st.container():
    st.subheader("Oops, You have incurred an error! :sob:")

with st.container():
    st_lottie(coding_error, height=460, key="Error 404")
