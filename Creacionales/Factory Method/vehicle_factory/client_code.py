"""3. Aqui se llama a la factory y se le pasa el tipo de vehiculo que se quiere crear."""


def client_vehicle_code(factory, vehicle_type):
    vehicle = factory.get_vehicle(vehicle_type) 
    print(vehicle.deliver())