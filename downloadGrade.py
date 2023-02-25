import os
import docx2txt
from docx import Document
import re
 
path = "a//a//"
dir_list = os.listdir(path)
 
#print("Files and directories in '", path, "' :")
#print(dir_list) # prints all files names

arr=[]

for i in dir_list:
    text = docx2txt.process(path+i).replace("\n","").split(" ")
    wordDoc = Document(path+i)

    term=[i.split("-")[0], len(text)]
    if(term not in arr):
        arr.append(term)
    
    c=0
    for table in wordDoc.tables: 
        for row in table.rows:
            for cell in row.cells:
                if(len(re.sub(r"[\n\t\s]*", "", cell.text))==0):
                    c+=1

    if(c>25):
        print("THIS GUY HAS "+str(c)+" EMPTY BOX(es): \t", term[0])


arr = sorted(arr, key = lambda x: x[1])
print("LENGTH: ", len(arr))
for i in range(int(len(arr)/4)):
    print(arr[i])
