## Part B Task 3
import re
import sys
import pandas as pd
#import nltk
#import os

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
for i in range(124): 
    data = preprocess(docIDs[0][i]) 
    
    flag = True    
    for keyword in keywords:
        keyword = keyword.lower()
        #parse data with spaces
        pattern = re.compile(r"\b" + keyword + r"\b") 
        #find the pattern in the data
        m = pattern.search(data) 
        if not m:
            flag = False
            break
            
        if flag:
            print(docIDs[1][i])
