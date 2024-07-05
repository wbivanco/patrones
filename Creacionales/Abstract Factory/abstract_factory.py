"""1. Aquí se define la clase base y los producto abstracto de la clase."""

from abc import ABC, abstractmethod


class UIAbstractFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_textbox(self):
        pass


class Button(ABC): # A diferencia de factory, aquí hereda de ABC
    @abstractmethod
    def paint(self):
        pass


class TextBox(ABC): # A diferencia de factory, aquí hereda de ABC
    @abstractmethod
    def paint(self):
        pass