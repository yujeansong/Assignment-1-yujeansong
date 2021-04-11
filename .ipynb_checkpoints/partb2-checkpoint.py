# Part B Task 2
import re
import os
import sys

#preprocess: filename -> parsed data
def preprocess(filename):
    fin = open(filename, 'r')
    
    data = fin.read() 
    data = re.sub(r"[^a-zA-z\s]", "", data) #remove non-alphabets 
    data = re.sub(r"[\s+]", " ", data) #space or spaces into single space
    data = data.lower() #make all the remained characters into lowercase
    
    fin.close()
    
    return data

print(preprocess(sys.argv[1]))