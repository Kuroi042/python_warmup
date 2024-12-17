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

def stati():
    if(len(sys.argv)!= 2):
        print("args errors")
        return
    else:
        citie_capital_name = sys.argv[1]
        for key , value in capital_cities.items():
                if( value== citie_capital_name):
                    capital_abv =  key
        for key , value in states.items():
            if(value  == capital_abv ):
                returnVal =  key
                print(returnVal)
        return
if __name__ ==  '__main__' :
      stati()


    
       
