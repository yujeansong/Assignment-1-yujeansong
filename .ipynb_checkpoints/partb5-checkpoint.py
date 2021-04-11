## Part B Task 5
import re
import os
import sys
import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfTransformer
from numpy import dot
from numpy.linalg import norm
from functools import reduce 

def preprocess(filename):
    fin = open(filename, 'r')
    
    data = fin.read() 
    data = re.sub(r"[^a-zA-z\s]", "", data) #remove non-alphabets 
    data = re.sub(r"[\s+]", " ", data) #space or spaces into single space
    data = data.lower() #make all the remained characters into lowercase
    
    fin.close()
    
    return data

#ids from csv
docIDs = pd.read_csv("partb1.csv", header = None)

#keywords parsing
keywords = sys.argv[1:]
if len(keywords) > 5:
    keywords = keywords[:5]
ps = nltk.stem.PorterStemmer()
keywords = list(map(lambda k: ps.stem(k), keywords))

#cosine similarity
def cossim(v1, v2):
    return dot(v1, v2) / (norm(v1) * norm(v2))

#search
results = []
for i in range(124): 
    data = preprocess(docIDs[0][i]).split() 
    data = list(map(lambda w: ps.stem(w), data))
      
    #the word no duplication
    terms = list(set(data))
    terms.sort()
    
    terms_cnt = [0,0]
    terms_cnt[0] = list(map(lambda t: data.count(t), terms))
    terms_cnt[1] = list(map(lambda t: keywords.count(t), terms))
    
    #change the form to python list
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(terms_cnt)
    tfidf_arr = tfidf.toarray()
    
    #save the results if every keyword searched
    found_flags = list(map(lambda k: 1 if k in data else 0, keywords))    
    if reduce(lambda acc, val: acc * val, found_flags, 1) > 0:
        results.append([docIDs[1][i], cossim(tfidf_arr[0], tfidf_arr[1])])
        
        
results = sorted(results, key = lambda r: r[1], reverse = True)
print("DocumentID", "score")
for result in results:
    print("%s %.4f" % tuple(result))
        
        
        
        


