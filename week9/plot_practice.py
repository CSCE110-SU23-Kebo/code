import matplotlib.pyplot as drawing
import os

# Step 1: Prepare Data
# Step 2: Customize and anotate
# St3 p 3: Plot

try:
    if not os.path.exists("classroom_charts"):
        os.mkdir("classroom_charts")
    os.chdir("classroom_charts")
except Exception as e:
    print(e)

# Drawing a line

# Step 1: Data
x_values = list([range(20)])
y_values = list([range(6,26)])

print(x_values)
print(y_values)

# Step 2
drawing.plot(x_values, y_values, marker="x", color ="r", linestyle="--")

drawing.xlabel("x values")
drawing.ylabel("y values")
drawing.yscale("linear")
drawing.grid()
drawing.legend()
drawing.title("Chat of numbers")

drawing.savefig("my_favorite_line.png")
drawing.show()