# graphics.py
import tkinter as tk

class Canvas:
    def __init__(self, width, height):
        self.root = tk.Tk()
        self.root.title("Canvas with Eraser")
        self.canvas = tk.Canvas(self.root, width=width, height=height, bg='white')
        self.canvas.pack()
        self._mouse_pressed = False
        self._mouse_x = 0
        self._mouse_y = 0

        self.canvas.bind("<B1-Motion>", self._on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self._on_mouse_release)

    def create_rectangle(self, x1, y1, x2, y2, color):
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='white')

    def set_color(self, item, color):
        self.canvas.itemconfig(item, fill=color)

    def moveto(self, item, x, y):
        coords = self.canvas.coords(item)
        if coords:
            width = coords[2] - coords[0]
            height = coords[3] - coords[1]
            self.canvas.coords(item, x, y, x + width, y + height)
 

    def get_mouse_pressed(self):
        return self._mouse_pressed

    def get_mouse_x(self):
        return self._mouse_x

    def get_mouse_y(self):
        return self._mouse_y

    def update(self):
        self.root.update_idletasks()
        self.root.update()

    def _on_mouse_drag(self, event):
        self._mouse_pressed = True
        self._mouse_x = event.x
        self._mouse_y = event.y

    def _on_mouse_release(self, event):
        self._mouse_pressed = False
