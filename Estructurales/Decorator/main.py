"""5. Implemanta la lógica de funcionamiento."""

from concrete_component import PlainText
from concrete_decorator import HTMLDecorator


plain_text = PlainText('Hola, mundo!')
print("Texto sin decorar: ", plain_text.render())

html_text = HTMLDecorator(plain_text)
print("Texto decorado: ", html_text.render())
