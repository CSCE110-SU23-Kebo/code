import matplotlib.pyplot as graph
import numpy

cycles = int(input("Enter the number of cycles: "))
angles = numpy.arange(0, cycles*numpy.pi, 0.1) # max angle in radians

# Step 1 : Prepare the data
sin_values = numpy.sin(angles)
cos_values = numpy.cos(angles)

# Step 2: Customize and annotate
graph.xlabel("Angles in radians")
graph.ylabel("Sine or Cosine")
graph.grid(color="r")
graph.plot(angles, sin_values, color='y')
graph.plot(angles, cos_values, color='m')
graph.legend()
graph.title(f"Plotting waves using NumPy for {cycles} cycles")

graph.savefig("sin-cos.png")
graph.show()

