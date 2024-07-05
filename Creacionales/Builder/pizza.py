"""1. Aqui se define la clase base del objeto."""

class Pizza:
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.topping = None

    def __str__(self):
        return f'Dough: {self.dough} | Suace {self.sauce} | Topping {self.topping}'