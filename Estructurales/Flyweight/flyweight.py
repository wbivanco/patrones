"""1. Especifica los atributos de cada objeto individual utilizando una fábrica.Esta fábrica controla la creación de objetos en función de los 
atributos de la clase."""

class ChessPieceFlyweight:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def display(self, position):
        print(f"Displaying {self.color} {self.name} at {position}") 