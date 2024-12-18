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
def parseArgv():
    if(len(sys.argv)<2):
        print("args error")
    
def Search_by_key():
    
    if(sys.argv[1] in states):
        statesAbv = states.get(sys.argv[1])
    for key , value in capital_cities.items():
        if(statesAbv == key):
            print(capital_cities.get(key))
    return     key   

def Search_by_value(name):
        
        for key , value in capital_cities.items():
            if(name ==  value):
                abv = key
        for keyS , valueS in states.items():
            if(abv  ==  valueS):
                res =  keyS
                # print(res)
        return res

def search():
    parseArgv()
    inputs =[elements.strip() for elements in sys.argv[1].split(",")]
    for item in inputs:
        if item  == "":
            continue
        found = False
        for key, value in capital_cities.items():
            if item.lower() == value.lower():
                print(item, "is the capital of", Search_by_value(value))
                found = True
                break

            elif item.lower() == key.lower():
                print(item, "is the abbreviation of", Search_by_value(value))
                found = True
                break
            
        for state, abbr in states.items():
            if item.lower() == state.lower():
                print(item, "is a state, and its capital is", capital_cities[abbr])
                found = True
                break
                
                    
        if not found:
                print(item, "is neither a capital nor the city")
    return

if __name__ == '__main__':
    # Search_by_value()
    search()