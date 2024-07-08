"""1. Defino la interfaz de los componentes que serán implementados por las clases."""

from abc import ABC, abstractmethod


class FileSystemComponent(ABC):
    @abstractmethod
    def show_details(self):
        pass