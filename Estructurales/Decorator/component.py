"""1. Es la interfaz de los objetos que pueden tener responsabilidades añadidas dinámicamente."""

from abc import ABC, abstractmethod


class Text(ABC):
    @abstractmethod
    def render(self):
        pass