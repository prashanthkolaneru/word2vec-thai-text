
# coding: utf-8

# In[1]:


import pandas as pd
import codecs
import gensim
import pythainlp
import nltk
from sklearn.feature_extraction.text import CountVectorizer
import json
import csv


# In[32]:


file = open(r'/home/prashanth/Untitled Document 1')
lines = file.readlines()
# print type(lines)
new_lines = []
for l in lines:
    tmp = l.strip().split("|")
    new_lines.append(tmp)
print type(new_lines)
print len(new_lines)
for l in new_lines:
    print len(l)
    print "|".join(l)


# In[33]:


from gensim.models import Word2Vec


# In[34]:


model = Word2Vec(new_lines, min_count=1)


# In[41]:


model.save('model.bin')
new_model = Word2Vec.load('model.bin')
print new_model
# words = list(model.wv.vocab)
# for w in words:
#     print(w)


# In[43]:


print(model['ครั้ง'])

