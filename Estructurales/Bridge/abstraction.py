"""2. Define como se manipularán las clases abstractas y las clases concretas."""

from implementor import Renderer


class Shape:
    def __init__(self, renderer):
        self.renderer = renderer        

    def draw(self):
        pass

    def resize(self, factor):
        pass


class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_shape("Circle")

    def resize(self, factor):
        self.radius *= factor