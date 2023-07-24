def clear_all_bits(number):
    """
    The function clears all the bits of a number using the bitwise AND operator.
    Mask: 0
    """
    mask = 0b0
    return bin(number & mask)


def clear_4msbits(number):
    """
    The function clears the four most significant bits of a number using the bitwise AND operator.
    Mask: 0
    """
    mask = 0b00001111
    return bin(number & mask)

def flip_all_bits(number):
    "THis function flips bits of a binaty number"
    mask = 0b11111111
    return bin(number ^ mask)


def set_3_msbits(number):
    mask = 0b1110000
    return( bin (number | mask))

    

def main():
    """
    This program performs bit masking 
    """
    number = int(input("Enter a number in binary: "), 2)
    print (f"{bin(number)[2:]} with all bits cleared is {clear_all_bits(number)}")
    print(f"Clear the 3 most significant bits: {clear_4msbits(number)}")
    print (f"{bin(number)[2:]} flipped {flip_all_bits(number)}")
    print(f"Set the 3 most significant bits: {set_3_msbits(number)}")

main()