class HotBeverage:
    price = 0.30  # Default price for all beverages
    name = "hot beverage"
    description_text = "Just some hot water in a cup."

    def __init__(self):
        self.price = self.price
        self.name = self.name

    def description(
            self):
        return self.description_text

    def __str__(self):
        return "name: {}\nprice: {:.2f}\ndescription: {}".format(self.name, self.price, self.description())

class Coffee(HotBeverage):
    price = 0.40
    name = "Coffee"
    description_text = "A coffee, to stay awake."


class Tea(HotBeverage):
    price = 0.30
    name = "Tea"
    description_text = "Just some hot water in a cup."


class Cappuccino(HotBeverage):
    price = 0.45
    name = "Cappuccino"
    description_text = "Un po di Italia nella sua tazza!"


# Example usage
coffee = Coffee()
tea = Tea()
cappuccino = Cappuccino()

print(coffee)
print( "XXX" )
print(tea)
print("XXX")
print(cappuccino)
