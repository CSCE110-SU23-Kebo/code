import matplotlib.pyplot as drawing
import random, os

try:
    if not os.path.exists("bar_charts"):
        os.mkdir("bar_charts")
    os.chdir("bar_charts")
except Exception as e:
    print(e)

# Step 1: Prepare the data
quizzes = ['quiz 1', 'quiz 2', 'quiz 3', 'quiz 4', 'quiz 5', 'quiz 6', 'quiz 7']
grades = [random.randint(50, 100) for grade in quizzes]

# Step 2: Customize and annotate
bars = drawing.barh(quizzes, grades, align="center", label="Quiz grades for CSCE 110")
drawing.ylabel("Quiz number")
drawing.xlabel("Quiz grade")
drawing.title("CSCE 110 Quiz grades")

for bar in bars:
    color = random.choice(['b', 'r', 'y', 'c', 'm'])
    bar.set_color(color)

drawing.savefig("quizzes_charts.png")
drawing.savefig("quizzes_charts.jpg")
drawing.savefig("quizzes_charts.pdf")

# Step 3: Show the plot
drawing.show()


