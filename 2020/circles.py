import turtle

def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
    turtle.pendown()

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(500)

draw_circle(tommy, "green", 20, 80, 0)
draw_circle(tommy, "blue", 20, 70, 0)
draw_circle(tommy, "yellow", 20, 60, 0)
draw_circle(tommy, "orange", 20, 50, 0)
draw_circle(tommy, "purple", 20, 40, 0)
draw_circle(tommy, "pink", 20, 30, 0)
draw_circle(tommy, "black", 20, 20, 0)
draw_circle(tommy, "gray", 20, 10, 0)
draw_circle(tommy, "red", 20, 0, 0)
draw_circle(tommy, "salmon", 20, -10, 0)
draw_circle(tommy, "maroon", 20, -20, 0)
draw_circle(tommy, "teal", 20, -30, 0)
draw_circle(tommy, "white", 20, -40, 0)
draw_circle(tommy, "navy", 20, -50, 0)
draw_circle(tommy, "olive", 20, -60, 0)
draw_circle(tommy, "lime", 20, -70, 0)


