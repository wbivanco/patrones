"""3. Aquí se encuentra el director que es opcional y permite crear los 
distintos objetos y devolverlos."""

class Cook:
    def make_pizza(self, builder):
        builder.set_dough()
        builder.set_sauce()
        builder.set_topping()
        return builder.pizza   