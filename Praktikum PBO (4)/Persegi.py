import turtle

class MyTurtle:
    def __init__(self, color, shape):
        self.t = turtle.Turtle()
        self.t.color(color)
        self.t.shape(shape)
        self.t.turtlesize(2)

    def maju(self, jarak):
        self.t.forward(jarak)

    def putar_kanan(self, sudut):
        self.t.right(sudut)

    def buat_persegi(self, ukuran):
        for _ in range(4):
            self.maju(ukuran)
            self.putar_kanan(90)

    def selesai(self):
        turtle.done()

turtle1 = MyTurtle("green", "turtle")

turtle1.buat_persegi(300)

turtle1.selesai()
