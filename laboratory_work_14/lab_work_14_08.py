# lab_work_08_oop.py

import tkinter as tk
from tkinter import messagebox
from math import exp, fabs

class TaylorSeries:
    def __init__(self, eps=1e-6, max_iter=1000):
        self.eps = eps
        self.max_iter = max_iter

    def calculate(self, x):
        term = 1.0
        total = term
        n = 1
        while fabs(term) > self.eps and n <= self.max_iter:
            term *= x / n
            total += term
            n += 1
        return total

class AnalyticFunction:
    def __init__(self, b=0.0):
        self.b = b

    def set_offset(self, b):
        self.b = b

    def calculate(self, x):
        return exp(x) + self.b

class GraphCanvas:
    def __init__(self, canvas, x_min, x_max, y_min, y_max, step=1.0):
        self.canvas = canvas
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.step = step
        self.width = canvas.winfo_reqwidth()
        self.height = canvas.winfo_reqheight()
        self.kx = self.width / (x_max - x_min)
        self.ky = self.height / (y_max - y_min)

    def update_params(self, x_min, x_max, y_min, y_max, step):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.step = step
        self.kx = self.width / (x_max - x_min)
        self.ky = self.height / (y_max - y_min)

    def draw_axes(self):
        self.canvas.delete("axes")
        self.canvas.create_rectangle(5, 5, self.width - 5, self.height - 5,
                                     outline="green", width=2, tags="axes")

        y = self.y_min
        y_pix = self.height
        flag = False
        while y <= self.y_max:
            text = f"{y:.2f}"
            self.canvas.create_line(0, y_pix, 10, y_pix, width=2, tags="axes")
            if flag:
                self.canvas.create_text(15, y_pix, text=text, anchor=tk.W, tags="axes")
            self.canvas.create_line(self.width - 10, y_pix, self.width, y_pix, width=2, tags="axes")
            if flag:
                self.canvas.create_text(self.width - 15, y_pix, text=text, anchor=tk.E, tags="axes")
            y += self.step
            y_pix -= self.step * self.ky
            flag = not flag

        x = self.x_min
        x_pix = 0
        flag = False
        while x <= self.x_max:
            text = f"{x:.2f}"
            self.canvas.create_line(x_pix, 0, x_pix, 10, width=2, tags="axes")
            if flag:
                self.canvas.create_text(x_pix, 15, text=text, anchor=tk.N, tags="axes")
            self.canvas.create_line(x_pix, self.height - 10, x_pix, self.height, width=2, tags="axes")
            if flag:
                self.canvas.create_text(x_pix, self.height - 15, text=text, anchor=tk.S, tags="axes")
            x += self.step
            x_pix += self.step * self.kx
            flag = not flag

    def draw_function(self, func, color, legend_text):
        points = []
        step_pix = 1.0 / self.kx
        x = self.x_min
        while x <= self.x_max:
            y = func.calculate(x)
            if y is not None and self.y_min <= y <= self.y_max:
                x_pix = self.kx * (x - self.x_min)
                y_pix = self.height - self.ky * (y - self.y_min)
                points.append((x_pix, y_pix))
            else:
                if len(points) >= 2:
                    self.canvas.create_line(points, fill=color, width=2, smooth=True, tags="graph")
                points = []
            x += step_pix
        if len(points) >= 2:
            self.canvas.create_line(points, fill=color, width=2, smooth=True, tags="graph")
        self.canvas.create_text(self.width - 120, 30 if legend_text == "Ряд Тейлора (e^x)" else 50,
                                text=legend_text, fill=color, anchor=tk.W, tags="graph")

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Графики функций – Лабораторная работа №8")
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
        self.root.resizable(False, False)

        self.x_min = -5.0
        self.x_max = 5.0
        self.y_min = -2.0
        self.y_max = 10.0
        self.step = 1.0
        self.offset = 0.0

        self.width = int(root.winfo_screenwidth() * 0.7)
        self.height = int(root.winfo_screenheight() * 0.7)

        self.create_widgets()
        self.create_math_objects()
        self.draw_all()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg="white")
        self.canvas.grid(row=0, column=0, columnspan=9)
        self.canvas.bind("<Button-1>", self.show_coordinates)

        labels = [
            ("X:", 1, 0, "x_entry", 1, 1),
            ("Y:", 2, 0, "y_entry", 2, 1),
            ("Xmin:", 1, 2, "xmin_entry", 1, 3),
            ("Xmax:", 1, 4, "xmax_entry", 1, 5),
            ("Ymin:", 2, 2, "ymin_entry", 2, 3),
            ("Ymax:", 2, 4, "ymax_entry", 2, 5),
            ("Шаг меток:", 1, 6, "step_entry", 1, 7),
            ("Смещение b:", 2, 6, "offset_entry", 2, 7)
        ]

        self.entries = {}
        for text, row_l, col_l, key, row_e, col_e in labels:
            lbl = tk.Label(self.root, text=text, width=10, fg="blue", font=("Arial", 10))
            lbl.grid(row=row_l, column=col_l, sticky='e')
            ent = tk.Entry(self.root, width=8, font=("Arial", 10))
            ent.grid(row=row_e, column=col_e, sticky='w' if col_e == 1 else 'e')
            self.entries[key] = ent

        self.entries["x_entry"].insert(0, "0.00")
        self.entries["y_entry"].insert(0, "0.00")
        self.entries["xmin_entry"].insert(0, str(self.x_min))
        self.entries["xmax_entry"].insert(0, str(self.x_max))
        self.entries["ymin_entry"].insert(0, str(self.y_min))
        self.entries["ymax_entry"].insert(0, str(self.y_max))
        self.entries["step_entry"].insert(0, str(self.step))
        self.entries["offset_entry"].insert(0, str(self.offset))

        btn_draw = tk.Button(self.root, width=15, bg="#ccc", text="Рисовать")
        btn_draw.grid(row=1, column=8)
        btn_draw.bind("<Button-1>", self.on_draw)

        btn_exit = tk.Button(self.root, width=15, bg="#ccc", text="Выход")
        btn_exit.grid(row=2, column=8)
        btn_exit.bind("<Button-1>", self.on_exit)

    def create_math_objects(self):
        self.taylor = TaylorSeries()
        self.analytic = AnalyticFunction(b=self.offset)
        self.graph_canvas = GraphCanvas(self.canvas, self.x_min, self.x_max,
                                        self.y_min, self.y_max, self.step)
        self.graph_canvas.width = self.width
        self.graph_canvas.height = self.height
        self.graph_canvas.update_params(self.x_min, self.x_max, self.y_min, self.y_max, self.step)

    def get_data(self):
        try:
            xmin = float(self.entries["xmin_entry"].get())
            xmax = float(self.entries["xmax_entry"].get())
            ymin = float(self.entries["ymin_entry"].get())
            ymax = float(self.entries["ymax_entry"].get())
            step = float(self.entries["step_entry"].get())
            offset = float(self.entries["offset_entry"].get())
            if xmin >= xmax or ymin >= ymax or step <= 0:
                messagebox.showwarning("Ошибка", "Xmax > Xmin, Ymax > Ymin, шаг > 0")
                return False
            self.x_min, self.x_max = xmin, xmax
            self.y_min, self.y_max = ymin, ymax
            self.step = step
            self.offset = offset
            self.analytic.set_offset(offset)
            return True
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректные числа")
            return False

    def draw_all(self):
        if not self.get_data():
            return
        self.graph_canvas.update_params(self.x_min, self.x_max, self.y_min, self.y_max, self.step)
        self.canvas.delete("all")
        self.graph_canvas.draw_axes()
        self.graph_canvas.draw_function(self.taylor, "blue", "Ряд Тейлора (e^x)")
        self.graph_canvas.draw_function(self.analytic, "red", f"Аналитическая: e^x + {self.offset:.2f}")

    def on_draw(self, event):
        self.draw_all()

    def show_coordinates(self, event):
        x_pix, y_pix = event.x, event.y
        x_user = self.x_min + x_pix / self.graph_canvas.kx
        y_user = self.y_min + (self.height - y_pix) / self.graph_canvas.ky
        self.entries["x_entry"].delete(0, tk.END)
        self.entries["y_entry"].delete(0, tk.END)
        self.entries["x_entry"].insert(0, f"{x_user:.2f}")
        self.entries["y_entry"].insert(0, f"{y_user:.2f}")

        if hasattr(self, "line_x"):
            self.canvas.delete(self.line_x)
            self.canvas.delete(self.line_y)
        self.line_x = self.canvas.create_line(0, y_pix, self.width, y_pix, dash=(3,5), fill="gray")
        self.line_y = self.canvas.create_line(x_pix, 0, x_pix, self.height, dash=(3,5), fill="gray")

    def on_exit(self, event):
        self.on_closing()

    def on_closing(self):
        if messagebox.askyesno("Выход", "Завершить работу?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()