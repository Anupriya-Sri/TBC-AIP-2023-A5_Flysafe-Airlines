#!/usr/bin/env python
# coding: utf-8

# In[11]:


import streamlit as st
from transformers import pipeline
import pandas as pd


# In[12]:


test_df = pd.read_excel("test.xlsx")


# In[13]:


st.write('SENTIMENT ANLAYSIS OF FLIGHT REVIEWS ')
classifier = pipeline("sentiment-analysis")
label = []
score = []
for review in test_df['comment']:
    result = classifier(test_df['comment'][0])
    label.append(result[0]['label'])
    score.append(result[0]['score'])


# In[14]:


st.write("REVIEWS 😁😍☺️❤️😊🙁😖😤😡")
st.write("REVIEWS SENTIMENT")

label


# In[15]:


st.write("REVIEWS 😁😍☺️❤️😊🙁😖😤😡")
st.write("REVIEWS SCORE")
score


# In[16]:


st.sidebar.markdown('We can analyze passenger reviews from this application')


# In[ ]:




