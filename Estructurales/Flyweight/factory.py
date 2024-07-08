"""2. Controla la creación de los objetos dado sus atributos."""

from flyweight import ChessPieceFlyweight


class ChessPieceFactory:
    _flyweights = {}

    @classmethod
    def get_flyweight(cls, name, color):
        key = (name, color)
        if not cls._flyweights.get(key):
            cls._flyweights[key] = ChessPieceFlyweight(name, color)
        return cls._flyweights[key]