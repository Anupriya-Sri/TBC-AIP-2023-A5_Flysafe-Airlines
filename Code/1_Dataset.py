#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
from transformers import pipeline
import pandas as pd
import wordcloud 

from wordcloud import WordCloud
import matplotlib.pyplot as plt


# In[3]:


st.title('FLY SAFE AIRLINE SENTIMENT ANALYSIS')
st.markdown('This application is all about analysis of the flight reviews of FLY SAFE AIRLINES ')


st.write('This app uses the Hugging Face Transformers [sentiment analyser](https://huggingface.co/course/chapter1/3?fw=tf) library to clasify the sentiment of your input as postive or negative. The web app is built using [Streamlit](https://docs.streamlit.io/en/stable/getting_started.html).')
st.write('*Note: it will take up to 30 seconds to run the app.*')


# In[4]:


uploaded_file = st.file_uploader("Choose a file")
    
if uploaded_file is not None:

            df = pd.read_csv('test.xlsx')


# In[ ]:




