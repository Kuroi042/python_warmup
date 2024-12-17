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
    if(len(sys.argv)==2 ):
        if(  sys.argv[1] in states):
            # print(str(sys.argv[1]))
            # print(states[sys.argv[1]])
        # for keyscity, valuecity  in capital_cities.items():
            if( states[sys.argv[1]] in capital_cities ):
                print(capital_cities[states[sys.argv[1]]]) 
            
        else:
            print("no args \n")
if __name__ == '__main__':
    printarg()
