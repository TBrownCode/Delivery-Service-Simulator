import csv
from distance_matrix import DISTANCE_MATRIX, get_distance

class Truck:
    def __init__(self, capacity=16, speed=18, mileage=0.0):
        self.capacity = capacity
        self.speed = speed
        self.packages = []
        self.mileage = mileage
        self.current_location = 0  # start at the hub 
        self.time = 8 * 60  # Start time in minutes (8:00 AM)
        self.distances = DISTANCE_MATRIX
    # initializes a truck object with attributes

    def calculate_distance(self, start, end):
        return get_distance(start, end)
    # calculates distance between two locations

    def distance_to_package(self, package):
        return self.calculate_distance(self.current_location, package.location_index)
    # calculates distance to package

    def find_nearest_package(self):
        return min(self.packages, key=self.distance_to_package)
    # finds the nearest package to current location

    def deliver_packages(self):
        while self.packages:
            next_package = self.find_nearest_package()
            distance = self.calculate_distance(self.current_location, next_package.location_index)
            self.mileage += distance
            travel_time = (distance / self.speed) * 60
            self.time += travel_time
            self.current_location = next_package.location_index
            self.packages.remove(next_package)
            next_package.status = "Delivered"
            next_package.delivery_time = self.get_current_time()

            print(f"Delivered package {next_package.package_id} to {next_package.address} at {next_package.delivery_time}")
            print(f"Truck mileage: {self.mileage:.1f}, Current time: {self.get_current_time()}")

        print(f"All packages delivered. Total mileage: {self.mileage:.1f}, Final time: {self.get_current_time()}")
    # delivers all packages on a truck

    def return_to_hub(self):
        distance_to_hub = self.calculate_distance(self.current_location, 0)
        travel_time = (distance_to_hub / self.speed) * 60
        self.mileage += distance_to_hub
        self.time += travel_time
        self.current_location = 0
        print(f"Truck returned to hub. Current time: {self.get_current_time()}, Mileage: {self.mileage:.1f}")
    
    # returns truck to the hub

    def start_second_run(self, packages):
        self.return_to_hub()
        self.packages = packages
        print(f"Truck loaded for second run. Current time: {self.get_current_time()}")
        self.deliver_packages()
    # starts the second delivery run

    def get_current_time(self):
        hours, minutes = divmod(int(self.time), 60)
        return f"{hours:02d}:{minutes:02d}"
    # gets the current time as a formatted string

    def load_package(self, package):
        if len(self.packages) < self.capacity:
            self.packages.append(package)
            return True
        return False
    # loads a package onto a truck

    def __str__(self):
        package_info = ', '.join([f"{p.address}" for p in self.packages])
        return f"Truck at location index {self.current_location}, Packages: {package_info}, Mileage: {self.mileage:.1f}, Time: {self.get_current_time()}"
    # a string representation of a truck object