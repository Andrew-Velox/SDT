from abc import ABC, abstractmethod
from ride import RideMatching, RideRequest


class User(ABC):
    def __init__(self,name,email,nid):
        self.name = name
        self.email = email
        self.nid = nid
        self.wallet = 0
    

    def display_profile(self):
        raise NotImplementedError




class Rider(User):
    def __init__(self,name,email,nid,current_location,inital_amount):
        super().__init__(name,email,nid)
        self.current_location = current_location
        self.wallet = inital_amount
        self.current_ride = None
    

    def display_profile(self):
        print(f"Name: {self.name} Email: {self.email}")
    
    def load_cash(self,amount):
        if amount > 0:
            self.wallet += amount
        else:
            print("Invalid amount. Please enter a positive value.")
    
    def update_location(self,current_location):
        self.current_location = current_location

    def request_ride(self,ride_sharing,destination,vehicle_type):
        ride_request = RideRequest(self, destination)
        ride_matching = RideMatching(ride_sharing.drivers)
        ride = ride_matching.find_driver(ride_request,vehicle_type)
        ride.rider = self
        self.current_ride = ride
        print(f"Ride requested from {self.current_location} to {destination} with vehicle type {vehicle_type}.")

    def show_current_ride(self):
        print(f"Current Ride Details:")
        print(f"Ride: {self.current_ride}")
        print(f"Driver: {self.current_ride.driver.name}")
        print(f"Start Location: {self.current_ride.start_location}")
        print(f"End Location: {self.current_ride.end_location}")    
        print(f"Total Fare: {self.current_ride.estimated_fare}")



class Driver(User):
    def __init__(self, name, email, nid, current_location):
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.wallet = 0;

    def display_profile(self):
        print(f"Driver Name: {self.name}")

    def accept_ride(self,ride):
        ride.set_driver(self)
        ride.start_ride()
    
    def reach_destination(self, ride):
        ride.end_ride()



# pathao = RideSharing("Pathao")
# rider1 = Rider("Alice", "alice@example.com", "NID123", "Location A", 100)
# driver1 = Driver("Bob", "bob@example.com", "NID456", "Location B")
# pathao.add_rider(rider1)
# pathao.add_driver(driver1)

# rider1.request_ride(pathao, "Destination X", "car")
# rider1.show_current_ride()

# driver1.rech_destination(rider1.current_ride)
# print(pathao) 