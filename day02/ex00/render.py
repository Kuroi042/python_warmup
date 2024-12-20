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
        exit()
    
def search():
    parseArg()
    
    with open("settings.py","r") as name:
    # print(name.read())
        for line in name:
            match = re.match(r'name\s*=\s*"(.*?)"', line)
            if(match):
                value =match.group(1)
                # print(value)
    if not value:
            exit()
    
    with open(sys.argv[1], "r") as cv:
        content  =  cv.read()
        update = re.sub(r"\{name}",value,content)
    with open("cv.html", "w") as new_file:
            new_file.write(update)   
search()
    

