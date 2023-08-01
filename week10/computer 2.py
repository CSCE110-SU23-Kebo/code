class Computer:
    def __init__(self):
        # Create a private attribute
        self.__memberPrice = 600
        # Create a public attribute
        self.regularPrice = 800

    def sell(self):
        """"
        This is a getter function
        """
        print(f"\nThe member price of the computer is {self.__memberPrice}")
        print(f"The regular price of the computer is {self.regularPrice}")

    def setMemberPrice(self, new_price):
        """
        This is a setter function
        @param new_price:
        @return:
        """
        self.__memberPrice = new_price


def main():
    chromebook = Computer()
    print(f"Regular price: {chromebook.regularPrice}")
    chromebook.sell()

    # Update the members price (This will fails)
    chromebook.__memberPrice = 300
    chromebook.sell()

    # Use the setter
    chromebook.setMemberPrice(300)
    chromebook.sell()


main()



