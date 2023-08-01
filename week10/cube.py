class Cube:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Sum(self):
        print(self.x + self.y)

    def get_x_y(self):
        return self.x, self.y


# creating list
cubes = []

# appending instances to list
cubes.append(Cube(2, 3))
cubes.append(Cube(12, 13))
cubes.append(Cube(22, 33))

for cube in cubes:
    # calling method
    cube.Sum()
    print(cube.get_x_y()) # Getter function for x and y
    print(cube)

# We can also access instances method
# as list[0].Sum() , list[1].Sum() and so on.
