"""1. Se puede definir la clase base en este archivo o llamado models o tambien se puede crear un directorio
donde se almacenaran los modelos en archivos individuales, esto es reocomendable en proyecto grandes."""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def deliver(self):
        pass


class Car(Vehicle):
    def __init__(self, model):
        self._model = model


    def deliver(self):
        return f"Auto {self._model} entregado"
    

class Truck(Vehicle):
    def __init__(self, model):
        self._model = model


    def deliver(self):
        return f"Camiòn {self._model} entregado"