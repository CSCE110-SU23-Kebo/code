class Computer:
    """This is the spec blueprint for a computer"""
    def __init__(self):
        "Constructor of the vehicle object"
        self.regularPrice = 800

    def sell(self):
        """This is a getter price"""
        print(f"The regular price of the computer is: ${self.regularPrice}")

    def setPrice(self, new_price):
        """This is a setter function """
        self.regularPrice = new_price

def main():
    chromebook = Computer()
    print(f"Regular price: ${chromebook.regularPrice}")
    # Set the price
    chromebook.setPrice(160)
    # Sell the computer
    chromebook.sell()
    
main()