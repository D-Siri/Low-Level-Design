from abc import ABC, abstractmethod
from vehicle_types import Vehicle


class Vehicles(ABC):
    def __init__(self, plate_number):
        self.plate_number = plate_number

    @abstractmethod
    def get_type(self):
        pass


class Car(Vehicles):

    def get_type(self):
        return Vehicle.CAR


class Motorcycles(Vehicles):

    def get_type(self):
        return Vehicle.MOTORCYCLE


class Trucks(Vehicles):

    def get_type(self):
        return Vehicle.TRUCK
