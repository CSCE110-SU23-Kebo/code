# An exception is an errors than occurs at runtime

import math
import sys

numbers = [2, 4, 5, 12.5, 0, 3.345, 78, 20203, 'pi', 78, 90]

for num in numbers:
    try:
        inverse = 1/num
        print(f"The inverse of {num} is {inverse}")
    except ZeroDivisionError as err:
        print(f"You cannot divide by Zero: {err}")
        print(f"Caught exception info: {sys.exc_info()}")
    except TypeError as err:
        print(f"You cannot divide 1 by a {type(num)}: {err}")
        print(f"Caught exception info: {sys.exc_info()}")
    else:
        print("All good!\n\n")
    finally:
        print("Division attempted")
