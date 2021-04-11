## Part B Task 1

import re
import pandas as pd
import sys

#Find the document ID form of 4 uppercase alphabets-optional 3 or 4 numbers
pattern = re.compile(r"[A-Z]{4}\-\d{3}[A-Z]?")  #raw string 
csv_filename = sys.argv[1]

fout = open(csv_filename, 'w')

for i in range(1,125):
    c_file = open("cricket/%03d.txt" % i, 'r') 
    
    m = pattern.search(c_file.read())
    
    if m:    #if valid 
        fout.write("cricket/%03d.txt,%s\n" %(i, m.group()))
            
    c_file.close()

fout.close()





