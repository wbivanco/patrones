"""2. Aquí se define los productos y subproductos de cada clase."""

from abstract_factory import Button, TextBox, UIAbstractFactory


class DarkButton(Button):
    def paint(self):
        print("Dark Button")    


class DarkTextBox(TextBox):
    def paint(self):
        print("Dark TextBox")


class LightButton(Button):
    def paint(self):
        print("Light Button")


class LightTextBox(TextBox):
    def paint(self):
        print("Light TextBox")


class LightUIFactory(UIAbstractFactory):
    def create_button(self):
        return LightButton()

    def create_textbox(self):
        return LightTextBox()
    

class DarkUIFactory(UIAbstractFactory):
    def create_button(self):
        return DarkButton()

    def create_textbox(self):
        return DarkTextBox()