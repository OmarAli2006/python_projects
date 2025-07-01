# Practica del patron de diseño factory en python
# Creado por: Omar Chanel Ali Fuertes

from re import M


class Vehicle:
    def drive(self):
        raise NotImplementedError("Subclase debe implementar por las subclases")

class Car(Vehicle):
    def drive(self):
        print("Conduciendo un coche")

class Truck(Vehicle):
    def drive(self):
        print("Conduciendo un camion")

class Bicycle(Vehicle):
    def drive(self):
        print("Conduciendo un bicicleta")

class Bus(Vehicle):
    def drive(self):
        print("Conduciendo un autobús")

class Motorcycle(Vehicle):
    def drive(self):
        print("Conduciendo un motocicleta")

# Fabrica de vehiculos
class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "truck":
            return Truck()
        elif vehicle_type == "bicycle":
            return Bicycle()
        elif vehicle_type == "bus":
            return Bus()
        elif vehicle_type == "motorcycle":
            return Motorcycle()
        else:
            raise ValueError("Tipo de vehiculo no reconocido")

if __name__ == "__main__":
    # Crear un coche
    car = VehicleFactory.create_vehicle("car")
    motorcycle = VehicleFactory.create_vehicle("motorcycle")
    bus = VehicleFactory.create_vehicle("bus")
    truck = VehicleFactory.create_vehicle("truck")
    bicycle = VehicleFactory.create_vehicle("bicycle")

    # Conducir un coche
    car.drive()
    motorcycle.drive()
    bus.drive()
    truck.drive()
    bicycle.drive()
    
