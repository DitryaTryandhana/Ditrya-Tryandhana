import tkinter as tk

# kelas induk Animal
class Animal:
    def make_sound(self):
        return "Some sound"
    
# kelas turunan Bird
class Bird(Animal):
    def make_sound(self):
        return "Tweet tweet"
    
# kelas turunan Dog
class Dog(Animal):
    def make_sound(self):
        return "Woof woof"

# kelas turunan Cat
class Cat(Animal):
    def make_sound(self):
        return "Meow meow"

# kelas turunan Frog
class Frog(Animal):
    def make_sound(self):
        return "Ribbit ribbit"

# Fungsi untuk menampilkan suara berdasarkan jenis hewan yang dipilih
def show_sound(animal):
    label_result.config(text=animal.make_sound())

# Membangun jendela utama menggunakan Tkinter
root = tk.Tk()
root.title("Polimorfisme di Tkinter")

# Label untuk menampilkan hasil suara
label_result = tk.Label(root, text="Klik salah satu tombol untuk mendengar suara hewan.", font=("Arial", 14))
label_result.pack(pady=20)

# Tombol untuk memilih Burung
button_bird = tk.Button(root, text="Burung", font=("Arial", 12), command=lambda: show_sound(Bird()))
button_bird.pack(pady=10)

# Tombol untuk memilih Anjing
button_dog = tk.Button(root, text="Anjing", font=("Arial", 12), command=lambda: show_sound(Dog()))
button_dog.pack(pady=10)

# Tombol untuk memilih Hewan umum
button_animal = tk.Button(root, text="Hewan Umum", font=("Arial", 12), command=lambda: show_sound(Animal()))
button_animal.pack(pady=10)

# Tombol untuk memilih Kucing
button_cat = tk.Button(root, text="Kucing", font=("Arial", 12), command=lambda: show_sound(Cat()))
button_cat.pack(pady=10)

# Tombol untuk memilih Katak
button_frog = tk.Button(root, text="Katak", font=("Arial", 12), command=lambda: show_sound(Frog()))
button_frog.pack(pady=10)

# Menjalankan aplikasi Tkinter
root.mainloop()
