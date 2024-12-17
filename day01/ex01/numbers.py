def openfile():
    with open("text.txt" ,"r") as f:
        data =  f.read()
    return data
def splitelement():
    f =  openfile()
    elements = f.split(",")
    return elements
def printelements():
    elements = splitelement()
    for numbers in  elements:
        print(numbers.strip() )
    return



if __name__ == '__main__':
    printelements()
