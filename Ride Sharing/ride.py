from datetime import datetime
from vehicle import Car, Bike

class RideSharing:
    def __init__(self,name):
        self.name = name
        self.riders = []
        self.drivers = []
        self.rides = []

    def add_rider(self, rider):
        self.riders.append(rider)
    def add_driver(self, driver):
        self.drivers.append(driver)


    def __str__(self):
        return(f"Ride Sharing Service: {self.name} with riders: {len(self.riders)} and drivers: {len(self.drivers)}")



class Ride:
    def __init__(self,start_location,end_location,vehicle):
        self.start_location = start_location
        self.end_location = end_location
        self.vehicle = vehicle
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = self.calculate_fare(vehicle.vehicle_type)

    def calculate_fare(self, vehicle):
        fare_per_km = {
            "car": 30,  # 30 currency units per km
            "bike": 20,   # 20 currency units per km
            "cng": 25     # 25 currency units per km
        }

        return fare_per_km.get(vehicle)

    def set_driver(self, driver):
        self.driver = driver
    
    def start_ride(self):
        self.start_time = datetime.now()
        
    def end_ride(self):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare
    
    def __repr__(self):
        return f"Ride from {self.start_location} to {self.end_location} with driver {self.driver.name} and rider {self.rider.name}."


class RideRequest:
    def __init__(self,rider,end_location):
        self.rider = rider
        self.end_location = end_location


class RideMatching:
    def __init__(self,driver):
        self.available_drivers = driver

    def find_driver(self,ride_request,vehicle_type):
        if len(self.available_drivers) == 0:
            print("No drivers available at the moment.")
        else:
            print("Looking for available drivers...")
            driver = self.available_drivers[0]  # Simplified for demo purposes


            if vehicle_type == "car":
                vehicle = Car("car", "ABC123", 100)
            elif vehicle_type == "bike":
                vehicle = Bike("bike", "XYZ456", 50)

            ride = Ride(ride_request.rider.current_location, ride_request.end_location,vehicle)
            
            driver.accept_ride(ride)
            return ride
