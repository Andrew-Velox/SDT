from ride import Ride, RideMatching, RideRequest,RideSharing
from users import Rider, Driver
from vehicle import Car, Bike

pathao = RideSharing("Pathao")
alice = Rider("Alice", "alice@example.com", "NID123", "Location A", 100)
bob = Driver("Bob", "bob@example.com", "NID456", "Location B")
pathao.add_rider(alice)
pathao.add_driver(bob)

alice.request_ride(pathao, "Destination X", "car")
bob.reach_destination(alice.current_ride)
alice.show_current_ride()