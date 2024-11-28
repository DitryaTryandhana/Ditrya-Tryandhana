import turtle

class MyTurtle:
    def __init__(self, color, shape):
        # Membuat objek turtle
        self.t = turtle.Turtle()
        self.t.color(color)
        self.t.shape(shape)

    def maju(self, jarak):
        # Method untuk menggerakkan turtle maju sesuai jarak yang ditentukan
        self.t.forward(jarak)

    def belok_kiri(self, sudut):
        # Method untuk memutar turtle ke kiri
        self.t.left(sudut)

    def buat_lingkaran(self, radius):
        # Method untuk menggambar lingkaran dengan radius tertentu
        self.t.circle(radius)

    def selesai(self):
        # Method untuk menyelesaikan gambar
        turtle.done()

# Membuat objek turtle dengan warna dan bentuk
turtle1 = MyTurtle("purple", "turtle")

# Menggambar lingkaran dengan radius 100
turtle1.buat_lingkaran(100)

# Menyelesaikan gambar
turtle1.selesai()
