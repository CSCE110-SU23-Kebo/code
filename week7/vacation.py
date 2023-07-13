"""
The open() function creates a file object / handle (a way of getting at the contents of the file).
The file object is also called a handle, it is used to read or write to the file.
filename is the path the file.
The mode is the file system permission.
"""
import os

"""os.chdir("/Users/davidkebo/Library/CloudStorage/GoogleDrive-davidkebo@tamu.edu/My Drive/Courses/CSCE-110/2023 SUMMER/code/code/week7")
print(os.listdir())"""

os.mkdir("summer_vacation")
os.chdir("summer_vacation")

print(f"What is the current path: {os.getcwd()}")
      
# Step 1: create a dictionary of travel destinations
destinations = {'San Miguel': 900, 'Tijuana':1200, 'Rio de Janeiro': 1500, 'Merida': 860}

# Step 2: create a file to store the destinations
travels = open("cities.txt", "w")

line = f"{'city name':<15} {'ticket price':<15}\n"
travels.write(line)

for city, price in destinations.items():
    line = f"{city:<15} ${price:<15}\n"
    travels.write(line)
print(f"All the destinations are saved!")

travels.close()