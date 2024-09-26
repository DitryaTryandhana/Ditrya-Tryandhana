import turtle

class MyTurtle:
    def __init__(self, color, shape, x, y): #membuat obyek turtle
        self.t = turtle.Turtle()
        self.t.color(color)
        self.t.shape(shape)
        self.t.penup()
        self.t.setpos(x, y)
        self.t.pendown()

    def maju(self, jarak):
        self.t.forward(jarak)

    def putar_kanan(self, sudut):
        self.t.right(sudut)

    def buat_bintang(self, ukuran):
        for _ in range(5):
            self.maju(ukuran)
            self.putar_kanan(144)

    def buat_bintang_berjejer(self, ukuran, jumlah, jarak):
        for _ in range(jumlah):
            self.buat_bintang(ukuran)
            self.t.penup()
            self.maju(jarak)
            self.t.pendown()

    def selesai(self):
        turtle.done()

turtle1 = MyTurtle("red", "turtle", -200, 0)
turtle1.buat_bintang_berjejer(100, 3, 100)

turtle2 = MyTurtle("yellow", "turtle", -200, 0)
turtle2.buat_bintang_berjejer(100, 3, 100)

turtle1.selesai()
