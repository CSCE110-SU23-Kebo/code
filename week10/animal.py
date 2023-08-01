class Cat:
    """
    In a class the behavior of the objects is defined in functions/methods
    The data is stored in attributes
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def identify(self):
        """
        This function identifies a cat object by name and age
        @return:
        """
        print(f"Cat identification\nName: {self.name}\nAge: {self.age}")

    def color(self):
        """
        This function prints the color of the cat object
        @return:
        """
        print(f"White")

    def movement(self):
        """
        This function prints the movement of the cat object
        @return:
        """
        print(f"Jump")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def identify(self):
        """
        This function identifies a cat object by name and age
        @return:
        """
        print(f"Dog identification\nName: {self.name}\nAge: {self.age}")

    def color(self):
        """
        This function prints the color of the cat object
        @return:
        """
        print(f"Brown")

    def movement(self):
        """
        This function prints the movement of the cat object
        @return:
        """
        print(f"Walk")


myCat = Cat("Kevin", 4)
myDog = Dog("Barker", 2)

for pet in (myCat, myDog):
    pet.identify()
    pet.color()
    pet.movement()
