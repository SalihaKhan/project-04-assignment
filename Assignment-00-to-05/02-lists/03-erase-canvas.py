import tkinter as tk
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

class Canvas:
    def __init__(self, width, height):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=width, height=height, bg='white')
        self.canvas.pack()
        self.last_click = (0, 0)
        self.canvas.bind('<Button-1>', self._store_click)
        
    def _store_click(self, event):
        self.last_click = (event.x, event.y)
        
    def get_last_click(self):
        return self.last_click
        
    def get_mouse_x(self):
        return self.canvas.winfo_pointerx() - self.canvas.winfo_rootx()
        
    def get_mouse_y(self):
        return self.canvas.winfo_pointery() - self.canvas.winfo_rooty()
        
    def create_rectangle(self, x1, y1, x2, y2, color):
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        
    def moveto(self, obj, x, y):
        self.canvas.coords(obj, x, y, x + ERASER_SIZE, y + ERASER_SIZE)
        
    def find_overlapping(self, x1, y1, x2, y2):
        return self.canvas.find_overlapping(x1, y1, x2, y2)
        
    def set_color(self, obj, color):
        self.canvas.itemconfig(obj, fill=color)
        
    def wait_for_click(self):
        self.canvas.bind('<Button-1>', self._store_click)
        self.root.wait_variable(self.root.new_variable())
        
    def is_button_pressed(self, button_num):
        # Not implemented in this simple version
        return True

def erase_objects(canvas, eraser):
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()
    
    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE
    
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
    
    for obj in overlapping_objects:
        if obj != eraser:
            canvas.set_color(obj, 'white')

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE
    
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')
    
    # Wait for initial click
    canvas.root.wait_variable(tk.BooleanVar())
    last_click_x, last_click_y = canvas.get_last_click()
    
    # Create eraser
    eraser = canvas.create_rectangle(
        last_click_x, 
        last_click_y, 
        last_click_x + ERASER_SIZE, 
        last_click_y + ERASER_SIZE, 
        'pink'
    )
    
    # Main loop
    def update():
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        canvas.moveto(eraser, mouse_x, mouse_y)
        erase_objects(canvas, eraser)
        canvas.root.after(50, update)
    
    update()
    canvas.root.mainloop()

if __name__ == '__main__':
    main()