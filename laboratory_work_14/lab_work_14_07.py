
import turtle as tr
import math

class CoordinateSystem:
    def __init__(self, x_min=-10, x_max=10, y_min=-3, y_max=5):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    def setup_window(self, width=800, height=400):
        tr.setup(width, height)
        tr.setworldcoordinates(self.x_min, self.y_min, self.x_max, self.y_max)
        tr.title("График кусочно-заданной функции")
        tr.speed(0)
        tr.hideturtle()
        tr.tracer(0, 0)

    def get_world_coords(self):
        return self.x_min, self.x_max, self.y_min, self.y_max

class AxisDrawer:
    def __init__(self, coord_system):
        self.cs = coord_system
        self.turtle = tr.Turtle()
        self.turtle.hideturtle()
        self.turtle.speed(0)
        self.turtle.color("black")

    def draw_axes(self):
        self.turtle.penup()
        self.turtle.goto(self.cs.x_min, 0)
        self.turtle.pendown()
        self.turtle.goto(self.cs.x_max, 0)
        self.turtle.penup()
        self.turtle.goto(0, self.cs.y_min)
        self.turtle.pendown()
        self.turtle.goto(0, self.cs.y_max)

    def draw_marks(self):
        for x in range(int(self.cs.x_min), int(self.cs.x_max) + 1):
            if x == 0:
                continue
            self.turtle.penup()
            self.turtle.goto(x, 0)
            self.turtle.pendown()
            self.turtle.goto(x, 0.2)
            self.turtle.penup()
            if x > 0:
                self.turtle.goto(x - 0.3, -0.6)
            else:
                self.turtle.goto(x - 0.3, -0.6)
            self.turtle.write(str(x), font=("Arial", 10, "normal"))

        for y in range(int(self.cs.y_min), int(self.cs.y_max) + 1):
            if y == 0:
                continue
            self.turtle.penup()
            self.turtle.goto(0, y)
            self.turtle.pendown()
            self.turtle.goto(0.2, y)
            self.turtle.penup()
            if y > 0:
                self.turtle.goto(-0.8, y - 0.2)
            else:
                self.turtle.goto(-0.8, y - 0.3)
            self.turtle.write(str(y), font=("Arial", 10, "normal"))

    def draw_arrows(self):
        self.turtle.penup()
        self.turtle.goto(self.cs.x_max + 0.2, 0)
        self.turtle.shape("arrow")
        self.turtle.stamp()
        self.turtle.goto(self.cs.x_max - 0.5, -0.8)
        self.turtle.write("X", font=("Arial", 14, "bold"))

        self.turtle.shape("arrow")
        self.turtle.tiltangle(90)
        self.turtle.goto(0, self.cs.y_max + 0.2)
        self.turtle.stamp()
        self.turtle.goto(0.3, self.cs.y_max - 0.5)
        self.turtle.write("Y", font=("Arial", 14, "bold"))
        self.turtle.tiltangle(0)

    def draw_all(self):
        self.draw_axes()
        self.draw_marks()
        self.draw_arrows()

class FunctionPlotter:
    def __init__(self, coord_system):
        self.cs = coord_system
        self.turtle = tr.Turtle()
        self.turtle.hideturtle()
        self.turtle.speed(0)
        self.turtle.color("red")
        self.turtle.width(2)

    @staticmethod
    def function(x):
        if -9 <= x <= -5:
            return -math.sqrt(4 - (x + 7) ** 2) + 2
        elif -5 <= x <= -4:
            return 2.0
        elif -4 <= x <= 0:
            return -x / 2
        elif 0 <= x <= math.pi:
            return math.sin(x)
        elif math.pi <= x <= 10:
            return x - math.pi
        else:
            return None

    def plot(self, steps=2000):
        step = (self.cs.x_max - self.cs.x_min) / steps
        x = self.cs.x_min
        self.turtle.penup()
        first = True
        while x <= self.cs.x_max:
            y = self.function(x)
            if y is not None and self.cs.y_min <= y <= self.cs.y_max:
                if first:
                    self.turtle.goto(x, y)
                    self.turtle.pendown()
                    first = False
                else:
                    self.turtle.goto(x, y)
            else:
                self.turtle.penup()
                first = True
            x += step

class GraphApp:
    def __init__(self):
        self.coord_system = CoordinateSystem()
        self.axis_drawer = AxisDrawer(self.coord_system)
        self.plotter = FunctionPlotter(self.coord_system)

    def run(self):
        self.coord_system.setup_window(width=800, height=400)
        self.axis_drawer.draw_all()
        self.plotter.plot()
        tr.update()
        tr.mainloop()

if __name__ == "__main__":
    app = GraphApp()
    app.run()