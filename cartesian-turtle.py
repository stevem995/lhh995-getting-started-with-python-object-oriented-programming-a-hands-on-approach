import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.setworldcoordinates(-300, -300, 300, 300)  # Set coordinate system

# Create turtle object
pen = turtle.Turtle()
pen.speed(0)  # Set drawing speed (0: fastest)
pen.hideturtle()

# Draw axes
pen.pensize(5)
pen.penup()
pen.goto(-300, 0)
pen.pendown()
pen.goto(300, 0)

pen.penup()
pen.goto(0, -300)
pen.pendown()
pen.goto(0, 300)

# # Draw grid lines
for i in range(-300, 301, 50):
    # Draw x axes
    pen.pensize(3)
    pen.penup()
    pen.goto(i, -10)
    if i != 0 :
        pen_ax_pos = pen.position()
        pen.goto(i-7, -30)
        pen.write(i)
        pen.goto(pen_ax_pos)
    pen.pendown()
    pen.goto(i, 10)

    pen.penup()
    pen.goto(-10, i)
    if i != 0 :
        pen_ax_pos = pen.position()
        pen.goto(15, i-7)
        pen.write(i)
        pen.goto(pen_ax_pos)
    pen.pendown()
    pen.goto(10, i)



# Example: Plotting a point
pen.penup()
# the middle of the graph
pen.goto(0, 0)  # Go to coordinates center
pen.dot(5, "red")  # Draw a red dot

# Keep window open until closed manually
turtle.done()
