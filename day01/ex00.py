def my_var():
    num = 42
    number =  "42"
    var = "quarante-deux "
    float_var = 42.0
    bolvar =  True
    listvar = {42:"quarante-deux"}
    mylist = [42]
    tuplepurple = (42,)
    myset = {"charaf",5 ,"charaf" ,42}
    print(str(num) +" is type = "+ str(type(num)))
    print(number +" is type = "+ str(type(number)))
    print(var +" is type = "+str( type(var)))
    print(str(float_var)+" is type = "+ str(type(float_var)))
    print(str(bolvar)+ " is typr = " +str(type(bolvar)))
    print(str(listvar)+ " is typr = " +str(type(listvar)))
    print(str(mylist)+ " is typr = " +str(type(mylist))) #
    print(str(tuplepurple)+ " is typr = " +str(type(tuplepurple)))  #for fixed value unchanged 
    print(str(myset)+ " is typr = " +str(type(myset))) # set of elements // unique element == remove dup



    # return 




if __name__ == '__main__':
    my_var()