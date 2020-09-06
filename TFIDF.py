# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 22:40:57 2020

@author: annam
"""

documents = ['the the universe has very many stars',

             'the galaxy contains many stars',

             'the cold breeze of winter made it very cold outside'
             ]

split_documents = []
for i,j in enumerate(documents):
    split_documentss = j.split()
    split_documents.append(split_documentss)
    split_documents[i] = [(word,split_documentss.count(word)) for word in split_documentss]
#print(len(documents))    

cleaned_documents_1 = []

    
for k in range(0,len(documents)):
    cleaned_document = []
    for d in split_documents[k]:
        if d not in cleaned_document:
            cleaned_document.append(d)
    cleaned_documents_1.append(cleaned_document)

normalized_freq1={}

for q in range(0,len(cleaned_documents_1)):
    sentence = split_documents[q]
    len_sente = len(sentence)
    for freq in cleaned_documents_1[q]:
        first1 = []
        first = float(freq[1]/len_sente)
        normalized_freq1.update({freq[0]:first})
        
print(len(normalized_freq1))

# Inverse Document Frequency 
        
N = len(documents)
print(N)

Inverse_document_frequency = []
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
df1["log_values"]=np.log(df1["values"])

# final TFIDF

print(normalized_freq1.values())

df1["TFIDF_keys"] = normalized_freq1
df1["TFIDF_values"] = normalized_freq1.values()







        
    



































