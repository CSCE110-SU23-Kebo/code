gas_price = 1.99 # global variable

def college_station_costco():
    """
    This is the first store
    """
    global gas_price
    #gas_price = 2.88
    print(f"The price is college_station_costco: {gas_price}")
    gas_price += 1
    print(f"The price is college_station_costco: {gas_price}")



def heb():
    """
    This is the first store
    """
    global gas_price
    #gas_price = 2.89
    print(f"The price is HEB: {gas_price}")
    gas_price += 1
    print(f"The price is HEB: {gas_price}")

college_station_costco()
heb()
