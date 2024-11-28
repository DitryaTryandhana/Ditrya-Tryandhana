import tkinter as tk
from math import pi
from tkinter import messagebox

class Shape:
    def area(self):
        return "Not implemented"
    
    def perimeter(self):
        return "Not implemented"
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * pi * self.radius

def calculate():
    try:
        shape_type = shape_var.get()
        if shape_type == "Rectangle":
            shape = Rectangle(int(entry_param1.get()), int(entry_param2.get()))
        elif shape_type == "Circle":
            shape = Circle(int(entry_param1.get()))
        else:
            raise ValueError("Invalid shape")
        
        label_result.config(text=f"Area: {shape.area():.2f}, Perimeter: {shape.perimeter():.2f}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def reset():
    """Fungsi untuk mereset semua input dan hasil."""
    shape_var.set("Rectangle")  # Reset pilihan bentuk ke Rectangle
    entry_param1.delete(0, tk.END)  # Hapus isi input Parameter 1
    entry_param2.delete(0, tk.END)  # Hapus isi input Parameter 2
    label_result.config(text="Area: Perimeter: ")  # Reset label hasil

# Membuat jendela utama
root = tk.Tk()
root.title("Overriding in Shapes")

# Pilihan bentuk
shape_var = tk.StringVar(value="Rectangle")
tk.Radiobutton(root, text="Rectangle", variable=shape_var, value="Rectangle").pack()
tk.Radiobutton(root, text="Circle", variable=shape_var, value="Circle").pack()

# Input Parameter 1
tk.Label(root, text="Parameter 1:").pack()
entry_param1 = tk.Entry(root)
entry_param1.pack()

# Input Parameter 2
tk.Label(root, text="Parameter 2 (if Rectangle):").pack()
entry_param2 = tk.Entry(root)
entry_param2.pack()

# Tombol Calculate
button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.pack()

# Tombol Reset
button_reset = tk.Button(root, text="Reset", command=reset)
button_reset.pack()

# Label hasil
label_result = tk.Label(root, text="Area: Perimeter: ")
label_result.pack()

# Menjalankan aplikasi
root.mainloop()
