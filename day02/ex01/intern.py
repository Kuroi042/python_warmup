class Intern:
    def __init__(self,name = "My name? I’m nobody, an intern, I have no name.", time = 0 ):
        self.name = name
        self.time  = time
    def __str__(self):
        return f"{self.name}"
         
    def Coffee(self):
            print("This is the worst coffee you ever tasted.")
    def work(self):
            if self.time >6:
                raise Exception ("ana gha wliya") 
            print("Sorry im just an intern khassni nmchi fhali")


# randIterm =  Intern()

# # charaf.Coffee()
# try:
#     randIterm.work()
# except Exception as e:
#      print(e)

charaf = Intern()
print(charaf)
charaf.Coffee()
try :
    charaf.work()
except Exception as e:
     print(e)


