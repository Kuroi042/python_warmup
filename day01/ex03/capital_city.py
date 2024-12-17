import sys
states = {
"Oregon" : "OR",
"Alabama" : "AL",
"New Jersey": "NJ",
"Colorado" : "CO"
}
capital_cities = {
"OR": "Salem",
"AL": "Montgomery",
"NJ": "Trenton",
"CO": "Denver"
}

def printarg():
    if(len(sys.argv)!=2):
        print("args error\n")
        return
    else :
        state_name  = sys.argv[1]
        state_abv =  states.get(state_name)
        if(state_abv in capital_cities ):
            print(capital_cities.get(state_abv))




if __name__ == '__main__':
    printarg()


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

def printarg():
    if(len(sys.argv)==2 ):
        if(  sys.argv[1] in states):
            print(str(sys.argv[1]))
            if( states[sys.argv[1]] in capital_cities ):
                print(capital_cities[states[sys.argv[1]]]) 
            
        else:
            print("no args \n")
if __name__ == '__main__':
    printarg()