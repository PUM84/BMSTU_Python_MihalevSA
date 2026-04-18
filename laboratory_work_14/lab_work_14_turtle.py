import turtle as tr
from math import sqrt, sin, pi

class FunctionPlotter:
    """Класс для построения графика кусочно-заданной функции с помощью turtle."""

    def __init__(self, x_range=(-10, 10), y_range=(-3, 5), pixels_per_unit=30):
        self.x_min, self.x_max = x_range
        self.y_min, self.y_max = y_range
        self.pixels_per_unit = pixels_per_unit
        self.width = int((self.x_max - self.x_min) * pixels_per_unit)
        self.height = int((self.y_max - self.y_min) * pixels_per_unit)
        self.screen = tr.Screen()
        self.screen.setup(self.width, self.height)
        self.screen.setworldcoordinates(self.x_min, self.y_min,
                                        self.x_max, self.y_max)
        self.screen.title("График функции")
        self.pen = tr.Turtle()
        self.pen.ht()
        self.pen.speed(0)
        tr.tracer(0, 0)

    @staticmethod
    def f(x):
        if -9 <= x <= -5:
            return -sqrt(4 - (x + 7)**2) + 2
        elif -5 < x <= -4:
            return 2
        elif -4 < x <= 0:
            return -x / 2
        elif 0 < x <= pi:
            return sin(x)
        elif pi < x <= 10:
            return x - pi
        else:
            return None

    def draw_axis(self, min_val, max_val, axis='X'):
        self.pen.up()
        if axis == 'X':
            self.pen.goto(min_val, 0)
            self.pen.down()
            self.pen.goto(max_val, 0)
        else:
            self.pen.goto(0, min_val)
            self.pen.down()
            self.pen.goto(0, max_val)

    def draw_marks(self, min_val, max_val, axis='X'):
        self.pen.up()
        for t in range(int(min_val), int(max_val) + 1):
            if t == 0:
                continue
            if axis == 'X':
                self.pen.goto(t, 0)
                self.pen.down()
                self.pen.goto(t, 0.2)
                self.pen.up()
                self.pen.goto(t - 0.2, -0.5)
            else:
                self.pen.goto(0, t)
                self.pen.down()
                self.pen.goto(0.2, t)
                self.pen.up()
                self.pen.goto(-0.7, t - 0.2)
            self.pen.write(str(t), font=("Arial", 10, "normal"))

    def draw_arrow(self, max_val, axis='X'):
        triangle = [(0.1, -0.1), (0, 0.3), (-0.1, -0.1)]
        self.pen.up()
        self.pen.goto(0, 0)
        self.pen.begin_poly()
        for pt in triangle:
            self.pen.goto(pt)
        self.pen.end_poly()
        arrow = self.pen.get_poly()
        tr.register_shape("myArrow", arrow)
        self.pen.shape("myArrow")
        self.pen.shapesize(1, 2, 1)
        self.pen.tiltangle(0 if axis == 'X' else 90)
        if axis == 'X':
            self.pen.goto(max_val + 0.2, 0)
            self.pen.stamp()
            self.pen.goto(max_val - 0.5, -1.0)
        else:
            self.pen.goto(0, max_val + 0.2)
            self.pen.stamp()
            self.pen.goto(0.2, max_val - 0.5)
        self.pen.write(axis, font=("Arial", 14, "bold"))

    def plot_function(self, n_points=2000):
        self.pen.color("red")
        self.pen.width(2)
        dx = (self.x_max - self.x_min) / n_points
        x = self.x_min
        y = self.f(x)
        self.pen.up()
        if y is not None:
            self.pen.goto(x, y)
            self.pen.down()
        while x <= self.x_max:
            x += dx
            y = self.f(x)
            if y is None:
                self.pen.up()
            else:
                if not self.pen.isdown():
                    self.pen.down()
                self.pen.goto(x, y)

    def draw_all(self):
        self.pen.color("black")
        self.pen.width(2)
        self.draw_axis(self.x_min, self.x_max, 'X')
        self.draw_marks(self.x_min, self.x_max, 'X')
        self.draw_arrow(self.x_max, 'X')
        self.draw_axis(self.y_min, self.y_max, 'Y')
        self.draw_marks(self.y_min, self.y_max, 'Y')
        self.draw_arrow(self.y_max, 'Y')
        self.plot_function()
        tr.update()
        tr.mainloop()

if __name__ == "__main__":
    plotter = FunctionPlotter()
    plotter.draw_all()