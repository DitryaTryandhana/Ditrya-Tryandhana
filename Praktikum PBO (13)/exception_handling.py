import tkinter as tk
from tkinter import messagebox

def divide_numbers():
    """Fungsi untuk membagi dua angka yang dimasukkan pengguna."""
    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        result = num1 / num2
        label_result.config(text=f"Result: {result}")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed.")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def reset_inputs():
    """Fungsi untuk mereset input dan hasil ke kondisi awal."""
    entry_num1.delete(0, tk.END)  # Hapus isi Number 1
    entry_num2.delete(0, tk.END)  # Hapus isi Number 2
    label_result.config(text="Result: ")  # Reset label hasil

# Membuat jendela utama
root = tk.Tk()
root.title("Exception Handling in Division")

# Label dan input untuk Number 1
tk.Label(root, text="Number 1:").pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

# Label dan input untuk Number 2
tk.Label(root, text="Number 2:").pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

# Tombol untuk melakukan pembagian
button_divide = tk.Button(root, text="Divide", command=divide_numbers)
button_divide.pack()

# Tombol untuk mereset input dan hasil
button_reset = tk.Button(root, text="Reset", command=reset_inputs)
button_reset.pack()

# Label untuk menampilkan hasil
label_result = tk.Label(root, text="Result: ")
label_result.pack()

# Menjalankan aplikasi
root.mainloop()
