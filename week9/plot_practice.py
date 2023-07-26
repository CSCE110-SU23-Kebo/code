import matplotlib.pyplot as drawing
import os

# Step 1: Prepare Data (Pandas or CSV)
# Step 2: Customize and anotate
# Step 3: Plot

try:
    if not os.path.exists("classroom_charts"):
        os.mkdir("classroom_charts")
    os.chdir("classroom_charts")
except Exception as e:
    print(e)

# Plot #1: Drawing a line
# Step 1
x_values = list([range(20)])
y_values = list([range(6,26)])
print(x_values)
print(y_values)
# Step 2
drawing.plot(x_values, y_values, marker="v", color ="r", linestyle=":")

# Plot #2: Drawing a cubic equation: y = 2x^3 + 6x^2 + 5x + 9
# Step 1
x_values = list(range(-60, 60))
y_values = [2*(x**3) + 6*(x**2) + 5*x + 9 for x in x_values]
# Step 2
drawing.plot(x_values, y_values, marker="o", color ="c", linestyle="-.")

drawing.xlabel("x values")
drawing.ylabel("y values")
drawing.yscale("linear")
drawing.grid()
drawing.legend()
drawing.title("Multiple equation charts")

drawing.savefig("multiple_charts.png")
drawing.savefig("multiple_charts.jpg")
drawing.savefig("multiple_charts.pdf")

# Step 3
drawing.show()