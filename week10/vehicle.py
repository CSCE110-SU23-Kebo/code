"""
Create a class for a Vehicle
"""


class Vehicle:
    """
    This is a class for a Vehicle object
    """
    # Class Attribute
    manufacturing_country = 'USA'

    def __init__(self, brand, model, gearbox, horse_power, price):
        """
        Vehicle class constructor
        @param brand:
        @param gearbox:
        @param horse_power:
        """
        self.brand = brand
        self.model = model
        self.gearbox = gearbox
        self.horsepower = horse_power
        self.price = price

    def navigate(self, directions):
        """
        Prints a list of directions
        @param directions:
        @return:
        """
        for direction in directions:
            print(direction)

    def get_price(self):
        """
        This function returns the price of a Vehicle
        @return:
        """
        return self.price

    def set_price(self, new_price=None):
        """
        This function sets/changes the price of an existing Vehicle
        @return:
        """
        self.price = new_price


class Bus(Vehicle):
    """
    This is a class for a Bus object that inherit for a Vehicle Class
    """

    def __init__(self, seats):
        super().__init__(brand='Collins', model='Single deck', gearbox='Manual', horse_power='800', price='120800')
        self.seats = seats


def print_vehicle(vehicle):
    """
    Prints a vehicle object data
    @param vehicle:
    @return:
    """
    print(
        f"Brand: {vehicle.brand:<10} Gearbox: {vehicle.gearbox:<10} Horsepower: {vehicle.horsepower:<10} Price: {vehicle.price:<10}")


def main():
    """
    Create multiple instance of the Vehicle class
    @return:
    """
    # Create a Vehicle instance - Ford 150
    garage = []
    pickup = Vehicle("Ford", "F-150", "Automatic", 450, 36000)
    sedan = Vehicle("Tesla", "Model 3", "Automatic", 271, 42000)
    print_vehicle(pickup)
    print(f"The price of the {pickup.model} is {pickup.get_price()}")
    pickup.set_price(46000)  # Set  or modifies

    print_vehicle(pickup)
    print_vehicle(sedan)
    print(pickup.manufacturing_country)
    print(sedan.manufacturing_country)

    # Create a Bus object:
    school_bus = Bus(40)
    print(f"Is Bus a subclass of Vehicle? {issubclass(Bus, Vehicle)}")
    print(f"Is school_bus an instance of Bus? {isinstance(school_bus, Bus)}")
    print(f"Is school_bus an instance of Vehicle? {isinstance(school_bus, Vehicle)}")
    print(f"Number of seats in the bus: {school_bus.seats}")
    print(f"Manufacturing country of the bus: {school_bus.manufacturing_country}")
    # print(f"Brand of the bus: {school_bus.brand}")
    print_vehicle(school_bus)


main()
