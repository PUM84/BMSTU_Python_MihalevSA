from tkinter import *
from tkinter.messagebox import *
from math import exp

class GraphApp:
    """Класс для построения графиков двух функций с помощью Tkinter."""

    def __init__(self, master):
        self.master = master
        master.title("Графика (класс)")
        master.protocol('WM_DELETE_WINDOW', self.window_deleted)
        master.resizable(False, False)

        Kp = 0.7
        self.MaxX = int(master.winfo_screenwidth() * Kp)
        self.MaxY = int(master.winfo_screenheight() * Kp)

        self.cv = Canvas(master, width=self.MaxX, height=self.MaxY, bg="white")
        self.cv.grid(row=0, columnspan=9)
        self.cv.bind('<Button-1>', self.show_xy)

        self.Xmin, self.Xmax = -5.0, 5.0
        self.Ymin, self.Ymax = -2.0, 10.0
        self.dX, self.dY = 1.0, 0.0
        self.ID1 = self.ID2 = 0
        self.update_scale()

        self.create_widgets()

    def update_scale(self):
        self.Kx = self.MaxX / abs(self.Xmax - self.Xmin)
        self.Ky = self.MaxY / abs(self.Ymax - self.Ymin)

    def create_widgets(self):

        Label(self.master, text="X:", width=10).grid(row=1, column=0, sticky='e')
        self.entX = Entry(self.master, width=5)
        self.entX.grid(row=1, column=1, sticky='w')
        self.entX.insert(0, '0')

        Label(self.master, text="Y:").grid(row=2, column=0, sticky='e')
        self.entY = Entry(self.master, width=5)
        self.entY.grid(row=2, column=1, sticky='w')
        self.entY.insert(0, '0')

        Label(self.master, text="Xmin:").grid(row=1, column=2, sticky='e')
        self.entXmin = Entry(self.master, width=5)
        self.entXmin.grid(row=1, column=3)
        self.entXmin.insert(0, str(self.Xmin))

        Label(self.master, text="Xmax:").grid(row=1, column=4, sticky='e')
        self.entXmax = Entry(self.master, width=5)
        self.entXmax.grid(row=1, column=5)
        self.entXmax.insert(0, str(self.Xmax))

        Label(self.master, text="Ymin:").grid(row=2, column=2, sticky='e')
        self.entYmin = Entry(self.master, width=5)
        self.entYmin.grid(row=2, column=3)
        self.entYmin.insert(0, str(self.Ymin))

        Label(self.master, text="Ymax:").grid(row=2, column=4, sticky='e')
        self.entYmax = Entry(self.master, width=5)
        self.entYmax.grid(row=2, column=5)
        self.entYmax.insert(0, str(self.Ymax))

        Label(self.master, text="Шаг меток:").grid(row=1, column=6, sticky='e')
        self.entDX = Entry(self.master, width=5)
        self.entDX.grid(row=1, column=7)
        self.entDX.insert(0, str(self.dX))

        Label(self.master, text="Смещение:").grid(row=2, column=6, sticky='e')
        self.entDY = Entry(self.master, width=5)
        self.entDY.grid(row=2, column=7)
        self.entDY.insert(0, str(self.dY))

        Button(self.master, text="Рисовать", command=self.draw).grid(row=1, column=8)
        Button(self.master, text="Выход", command=self.window_deleted).grid(row=2, column=8)

    def get_data(self):
        try:
            self.Xmax = float(self.entXmax.get())
            self.Xmin = float(self.entXmin.get())
            self.Ymax = float(self.entYmax.get())
            self.Ymin = float(self.entYmin.get())
            self.dX = float(self.entDX.get())
            self.dY = float(self.entDY.get())
            if self.Xmin >= self.Xmax or self.Ymin >= self.Ymax or self.dX <= 0:
                raise ValueError
        except:
            showwarning("Ошибка", "Xmax > Xmin; Ymax > Ymin; Шаг меток > 0")
            return False
        self.update_scale()
        return True

    def draw(self):
        self.cv.delete("all")
        if not self.get_data():
            return
        self.plot_axes()
        self.draw_function(self.y_function, 'blue')
        self.draw_function(self.z_function, 'red')

    def plot_axes(self):

        self.cv.create_rectangle(5, 5, self.MaxX-5, self.MaxY-5,
                                 outline="green", width=2, fill="white")
        y = self.Ymin
        y_pix = self.MaxY
        flg = False
        while y < self.Ymax:
            textY = str(round(y, 2))
            self.cv.create_line(0, y_pix, 10, y_pix, width=2)
            if flg:
                self.cv.create_text(15, y_pix, text=textY, anchor=W)
            self.cv.create_line(self.MaxX-10, y_pix, self.MaxX, y_pix, width=2)
            if flg:
                self.cv.create_text(self.MaxX-15, y_pix, text=textY, anchor=E)
            y += self.dX
            y_pix -= self.dX * self.Ky
            flg = not flg

        x = self.Xmin
        x_pix = 0
        flg = False
        while x < self.Xmax:
            textX = str(round(x, 2))
            self.cv.create_line(x_pix, 0, x_pix, 10, width=2)
            if flg:
                self.cv.create_text(x_pix, 15, text=textX, anchor=N)
            self.cv.create_line(x_pix, self.MaxY-10, x_pix, self.MaxY, width=2)
            if flg:
                self.cv.create_text(x_pix, self.MaxY-15, text=textX, anchor=S)
            x += self.dX
            x_pix += self.dX * self.Kx
            flg = not flg

    def y_function(self):
        """Ряд Тейлора для exp(x) (с заданной точностью)."""
        eps = 0.0001
        points = []
        x = self.Xmin
        while x <= self.Xmax:
            an = 1.0
            s = an
            n = 1
            while abs(an) > eps:
                an *= x / n
                s += an
                n += 1
            points.append((x, s))
            x += 1 / self.Kx
        return points

    def z_function(self):
        """Точная функция exp(x) + dY."""
        points = []
        x = self.Xmin
        while x <= self.Xmax:
            points.append((x, exp(x) + self.dY))
            x += 1 / self.Kx
        return points

    def draw_function(self, func, color):
        points = func()
        pix_points = []
        for x, y in points:
            px = self.Kx * (x - self.Xmin)
            py = self.MaxY - self.Ky * (y - self.Ymin)
            pix_points.append((px, py))
        self.cv.create_line(pix_points, fill=color)

    def show_xy(self, event):
        x = event.x
        y = event.y
        real_x = self.Xmin + x / self.Kx
        real_y = self.Ymin + (self.MaxY - y) / self.Ky
        self.entX.delete(0, END)
        self.entX.insert(0, f"{real_x:.2f}")
        self.entY.delete(0, END)
        self.entY.insert(0, f"{real_y:.2f}")
        self.cv.delete(self.ID1)
        self.cv.delete(self.ID2)
        self.ID1 = self.cv.create_line(0, y, self.MaxX, y, dash=(3,5))
        self.ID2 = self.cv.create_line(x, 0, x, self.MaxY, dash=(3,5))

    def window_deleted(self):
        if askyesno("Выход", "Завершить работу?"):
            self.master.destroy()

if __name__ == "__main__":
    root = Tk()
    app = GraphApp(root)
    root.mainloop()