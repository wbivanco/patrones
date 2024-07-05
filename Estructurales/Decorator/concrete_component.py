"""2. Es una clase que implementa el componente, definiendo un objeto al que se le pueden añadir responsabilidades adicionales."""

from component import Text


class PlainText(Text):
    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text   