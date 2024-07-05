"""2. Aque se crean los objetos, para ello se una clase con un mètodo abstracto, que se 
encarga de crear los vehiculos."""

from abc import ABC, abstractmethod
from .product import Car, Truck


class VehicleFactory(ABC):
    @abstractmethod
    def get_vehicle(self, vehicle_type):
        pass