def openfile(): #read file
    with open("text.txt" ,"r") as f:
        data =  f.read()
    return data
 
def splitelement(): # split elements ","
    f =  openfile()
    elements = f.split(",")
    return elements

def printelements():  #print each elements inside the list
    elements = splitelement()
    for line in  elements: 
        print(line)
    return



if __name__ == '__main__':
    printelements()
