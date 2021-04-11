## Part B Task 4
import re
import pandas as pd
import os
import sys
import nltk

#preprocess: filename -> parse data
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
#get data in docIDs each row of first column 
ps = nltk.stem.PorterStemmer()
keywords = list(map(lambda k: ps.stem(k), keywords))


#search
for i in range(124): 
    data = preprocess(docIDs[0][i]).split()
    data = list(set(data))
    data = list(map(lambda w: ps.stem(w), data))
    
    flag = True    
    for keyword in keywords:
        if keyword not in data:
            flag = False
            break
        if flag:
            print(docIDS[1][i])