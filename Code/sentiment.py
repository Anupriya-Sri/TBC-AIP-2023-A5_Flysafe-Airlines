#!/usr/bin/env python
# coding: utf-8

# In[44]:


import streamlit as st
from transformers import pipeline
import pandas as pd
import wordcloud 
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# In[54]:


st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://tse2.mm.bing.net/th?id=OIP.W2v-evsXMt2HRAtDl-AlmQHaEs&pid=Api&P=0")
    }
   .sidebar .sidebar-content {
        background: url("")
    }
    </style>
    """,
    unsafe_allow_html=True
)


# In[46]:


st.title('SENTIMENT ANALYZER APPLICATION')
st.title('FLY SAFE AIRLINE SENTIMENT ANALYSIS')
st.markdown('This application is all about analysis of the flight reviews of FLY SAFE AIRLINES ')

st.write('This app uses the Hugging Face Transformers [sentiment analyser](https://huggingface.co/course/chapter1/3?fw=tf) library to clasify the sentiment of your input as postive or negative. The web app is built using [Streamlit](https://docs.streamlit.io/en/stable/getting_started.html).')
st.write('*Note: it will take up to 30 seconds to run the app.*')

form = st.form(key='sentiment-form')
user_input = form.text_area('Enter your text')
submit = form.form_submit_button('Submit')

if submit:
    classifier = pipeline("sentiment-analysis")
    result = classifier(user_input)[0]
    print(result)
    label = result['label']
    score = result['score']

    if label == 'POSITIVE':
        st.success(f'{label} sentiment (score: {score})')
    else:
        st.error(f'{label} sentiment (score: {score})')


# In[ ]:





# In[23]:





# In[ ]:





# In[14]:





# In[47]:


st.write("REVIEWS 😁😍☺️❤️😊🙁😖😤😡")


# In[48]:


st.write("REVIEWS SCORE")


# In[53]:





st.sidebar.markdown('We can analyze passenger reviews from this application')

st.sidebar.markdown('Positive😊/Negative😡') 
#st.write(data.query('comment==@tweets')[['text']].sample(1).iat[0,0])
#st.write(data.query('comment==@tweets')[['text']].sample(1).iat[0,0]).iat[0,0])
#st.write(data.query('comment==@tweets')[['text']].sample(1)
#select=st.sidebar.selectbox("Visualization of Tweets",['Histogram','wordcloud','pie chart'],key=1)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




