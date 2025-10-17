from math import sqrt, sin, pi
import turtle as tr

def function(x):
    y = 0.0
    if -9 <= x <= -5:
        y = -sqrt(4 - (x + 7)**2) + 2
    elif -5 <= x <= -4:
        y = 2
    elif -4 <= x <= 0:
        y = -x / 2
    elif 0 <= x <= pi:
        y = sin(x)
    elif pi <= x <= 10:
        y = x - pi
    else:
        y = None
    return y

def plot_axis(min_value, max_value, ax="X"):
    tr.up()
    if ax == "X":
        begin = (min_value, 0)
        end = (max_value, 0)
    else:
        begin = (0, min_value)
        end = (0, max_value)
    tr.goto(begin)
    tr.down()
    tr.goto(end)

def plot_mark(min_value, max_value, ax="X"):
    tr.up()
    for t in range(min_value, max_value + 1):
        if t == 0:
            continue
        if ax == "X":
            point_begin = (t, 0)
            point_end = (t, 0.2)
            if t > 0:
                point_width = (t - 0.2, -0.5)
            else:
                point_width = (t - 0.3, -0.5)
        else:
            point_begin = (0, t)
            point_end = (0.2, t)
            if t > 0:
                point_width = (-0.7, t - 0.2)
            else:
                point_width = (-0.7, t - 0.3)
        tr.goto(point_begin)
        tr.down()
        tr.goto(point_end)
        tr.up()
        tr.goto(point_width)
        tr.write(str(t), font=("Arial", 10, "normal"))


def plot_arrow(max_value, ax="X"):
    triangle = [(0.1, -0.1), (0, 0.3), (-0.1, -0.1)]
    tr.up()
    tr.goto(0, 0)
    tr.begin_poly()
    for couple in triangle:
        tr.goto(couple)
    tr.end_poly()
    arrow = tr.get_poly()
    tr.register_shape("myArrow", arrow)
    tr.resizemode("myArrow")
    tr.shapesize(1, 2, 1)
    if ax == "X":
        tr.tiltangle(0)
        tr.goto(max_value + 0.2, 0)
        point_width = (max_value - 0.5, -1.0)
    else:
        tr.tiltangle(90)
        tr.goto(0, max_value + 0.2)
        point_width = (0.2, max_value - 0.5)
    tr.stamp()
    tr.goto(point_width)
    tr.write(ax, font=("Arial", 14, "bold"))

def plot_function(min_value, max_value, n_max=1000):
    tr.color("red")
    tr.width(2)
    dx = (max_value - min_value) / n_max

    x = min_value
    y = function(x)
    tr.up()
    if y is not None:
        tr.goto(x, y)
        tr.down()

    while x <= max_value:
        x = x + dx
        y = function(x)
        if y is None:
            tr.up()
            continue
        else:
            if not tr.isdown():
                tr.down()
            tr.goto(x, y)

if __name__ == "__main__":
    aX = (-10, 10)
    aY = (-3, 5)

    pixels_per_unit = 30
    Dx = int((aX[1] - aX[0]) * pixels_per_unit)  # 20 * 30 = 600
    Dy = int((aY[1] - aY[0]) * pixels_per_unit)  # 8 * 30 = 240

    tr.setup(Dx, Dy)
    tr.reset()

    tr.setworldcoordinates(aX[0], aY[0], aX[1], aY[1])

    tr.title("График функции")
    tr.width(2)
    tr.color("black", "black")

    tr.ht()
    tr.tracer(0, 0)

    plot_axis(aX[0], aX[1], "X")
    plot_mark(aX[0], aX[1], "X")
    plot_arrow(aX[1], "X")

    plot_axis(aY[0], aY[1], "Y")
    plot_mark(aY[0], aY[1], "Y")
    plot_arrow(aY[1], "Y")

    plot_function(-9, 10, 2000)

    tr.update()
    tr.mainloop()