"""4. Aqui se crean las clases concretas que heredan de la clase abstracta 
creada en el archivo creator.py"""

from .product import Car, Truck
from .creator import VehicleFactory


class CarFactory(VehicleFactory):
    def get_vehicle(self, vehicle_type):
        return Car(vehicle_type)


class TruckFactory(VehicleFactory):
    def get_vehicle(self, vehicle_type):
        return Truck(vehicle_type)