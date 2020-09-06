# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 22:40:57 2020

@author: annam
"""

"""
documents = ['the the universe has very many stars',

             'the galaxy contains many stars',

             'the cold breeze of winter made it very cold outside'
             
             ]
"""

documents = ['The car is driven on the road',
            
             'The truck is driven on the highway']
split_documents = []
for i,j in enumerate(documents):
    split_documentss = j.split()
    print(split_documentss)
    split_documents.append(split_documentss)
    print(split_documents)
    split_documents[i] = [(word,split_documentss.count(word)) for word in split_documentss]
    

cleaned_documents_1 = []

    
for k in range(0,len(documents)):
    cleaned_document = []
    for d in split_documents[k]:
        
        if d not in cleaned_document:
            cleaned_document.append(d)
    cleaned_documents_1.append(cleaned_document)

normalized_freq1={}

for q in range(0,len(cleaned_documents_1)):
    sentence = cleaned_documents_1[q]
    print(sentence)
    len_sente = len(sentence)
    print(len_sente)
    for freq in cleaned_documents_1[q]:
        first = float(freq[1]/len_sente)
        normalized_freq1.update({freq[0]:first})
    
      
        
print(len(normalized_freq1))

# Inverse Document Frequency 
        
N = len(documents)
print(N)
import pandas as pd 


cleaned_dup = []

for t in range(0, len(documents)):
    sentence = cleaned_documents_1[t]
    sum=0
    #print(sentence)
    for each in sentence:
        keywords = each[0]
        cleaned_dup.append(keywords)
 
words=cleaned_dup

import numpy as np

df=pd.DataFrame(data=words,columns=["words"])
   
group=df.pivot_table(index=["words"],aggfunc = "size")
df1 = pd.DataFrame(data=group.to_frame())
df1["values"] = N/df1
df1["IDF_log_values"]=np.log10(df1["values"])
df1["normalized_freq"]=normalized_freq1.values()

# final TFIDF


df1["TFIDF_value"]=df1["normalized_freq"]*df1["IDF_log_values"]


##################  OR ########################

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
x = vectorizer.fit_transform(documents)
m=vectorizer.get_feature_names()
print(x.shape)






















