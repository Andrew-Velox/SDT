from abc import ABC, abstractmethod
class Vehicle(ABC):

    speed = {
        "car": 60,  # km/h
        "bike": 40,  # km/h
        "cng": 50   # km/h
    }
    def __init__(self,vehicle_type,license_plate,rate):
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate = rate


class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate):
        super().__init__(vehicle_type, license_plate, rate)

class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate):
        super().__init__(vehicle_type, license_plate, rate)

