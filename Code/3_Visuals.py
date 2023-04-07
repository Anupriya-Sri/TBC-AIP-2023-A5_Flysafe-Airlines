#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
from PIL import Image

image = Image.open('download1.png')

st.image(image, caption='Wordcloud')


# In[3]:


image2 = Image.open('download2.png')

st.image(image2, caption='Wordcloud')


# In[4]:


image3 = Image.open('download3.png')

st.image(image3, caption='Wordcloud')


# In[5]:


image4 = Image.open('download4.png')

st.image(image4, caption='Wordcloud')


# In[ ]:




