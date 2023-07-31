"""
Write a program to draw a Barnsley Fern using a transformation of point.
"""

import random
import matplotlib.pyplot as drawing


def fractal(iterations):
    """
    This function generates multiple points for the Barnsley fractal based on the number of iterations
    @param iterations:
    @return:
    """

    # Data the x, y (0, 0)
    # This is the first point
    x = 0
    y = 0

    # Data for x and y
    x_axis = [x]
    y_axis = [y]

    for i in range(iterations):

        # Generate a random number between and 0 and 1 or 0 and 100%
        probability = random.random()

        # Transformation 1: for the 85% (Successively smaller leaflets)
        if probability <= 0.85: #[0, 0.85]
            x = 0.85 * x + 0.04 * y
            y = -0.04 * x + 0.85 * y + 1.6

        # Transformation 2: for the 7%
        elif probability <= 0.92: # (0.85, 0.92]
            x = 0.2 * x + -0.26 * y
            y = 0.23 * x + 0.22 * y + 1.6

        # Transformation 3: for the 7%
        elif probability <= 0.99: # (0.92, 0.99]
            x = -0.15 * x + 0.28 * y
            y = 0.26 * x + 0.24 * y + 0.44

        # Transformation 4: for 1% (0.99, 1) (Stem)
        else:
            x = 0
            y = 0.16 * y

        # After the transformation add the points to the list of coordinates
        x_axis.append(x)
        y_axis.append(y)

    # Return the list of coordinates (x_axis, y_axis)
    return x_axis, y_axis


def main():
    iterations = int(input('What is the number of iterations? '))
    x_axis, y_axis = fractal(iterations)
    drawing.scatter(x_axis, y_axis, s=2, color='green')
    drawing.title("Barnsley Fern Fractal")
    drawing.show()


main()

