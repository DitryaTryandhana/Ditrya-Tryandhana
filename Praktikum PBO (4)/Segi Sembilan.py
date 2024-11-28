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

    def buat_poligon(self, ukuran):
        for _ in range(9):
            self.maju(ukuran)
            self.putar_kanan(40)

    def selesai(self):
        turtle.done()

turtle1 = MyTurtle("blue", "turtle")

turtle1.buat_poligon(100)

turtle1.selesai()
