from collections import namedtuple

import math
import streamlit as st
import extra_streamlit_components as stx
from time import sleep

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

cookie_manager = stx.CookieManager(key="main_auth_cookie_manager")


with st.echo(code_location='below'):
    for idx in range(2):
        st.info(idx)
