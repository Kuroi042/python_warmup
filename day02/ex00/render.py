#setting.py container the name
#mycv.template is the file where we gonna edit
#replace the name in cv.template with the name in setting.py
#write the result in a file.html
 
import sys
import os
import re
def parseArg():
    if(len(sys.argv)!=2):
        print("args error")
        exit
    
def search():
    parseArg()
    cv = open(sys.argv[1], "r")
    with open("settings.py","r") as name:
    # print(name.read())
        for line in name:
            match = re.match(r'name\s*=\s*"(.*?)"', line)
            if(match):
                name =match.group(1)
    for line in cv:
            match = re.sub()
            
            
            
search()
    

