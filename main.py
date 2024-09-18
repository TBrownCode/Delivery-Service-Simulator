# Tyler Brown || stid: 0120204083

import csv 
from package import Package
from truck import Truck
from distance_matrix import get_distance
from user_interface import UserInterface

class HashMap:
    def __init__(self):
        self.size = 50
        self.map = [[] for i in range(self.size)] 
    #creates a 2d array of lists with 50 spots

    def _hash(self, key):
        return hash(key) % self.size
    #hashes a key in order to be placed into the hash map

    def add(self, package_id, address, deadline, city, zip_code, weight, status):
        key = self._hash(package_id)
        if self.map[key]:
            for item in self.map[key]:
                if item[0] == package_id:
                    item[1:] = [address, deadline, city, zip_code, weight, status]
                    return
        self.map[key].append([package_id, address, deadline, city, zip_code, weight, status])
        #checks if the package id is in the hash map already, if it is, the parameters are appended to the end of that existing list
        #else the hashed package id's info is added to the map under its key

    def get(self, package_id):
        key = self._hash(package_id)
        for item in self.map[key]:
            if item[0] == package_id:
                return item[1:]
        return None
    # returns info stored under the the package id's key in the hashmap

    def update_status(self, package_id, new_status):
        key = self._hash(package_id)
        for item in self.map[key]:
            if item[0] == package_id:
                item[6] = new_status
                return True
        return False
    # checks if package id is in the hasmap if so it updates the status variable

def load_packages(filename, address_to_index):
    packages = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            location_index = address_to_index.get(row[1], 0)  # Default to hub (0) if address not found
            package = Package(*row, location_index)
            packages.append(package)
    return packages
# goes through the package csv and makes package objects with an added location index from the address to index dictionary

address_to_index = {
    "4001 South 700 East": 0,  # Western Governors University
    "1060 Dalton Ave S": 1,  # International Peace Gardens
    "1330 2100 S": 2,  # Sugar House Park
    "1488 4800 S": 3,  # Taylorsville-Bennion Heritage City Gov Off
    "177 W Price Ave": 4,  # Salt Lake City Division of Health Services
    "195 W Oakland Ave": 5,  # South Salt Lake Public Works
    "2010 W 500 S": 6,  # Salt Lake City Streets and Sanitation
    "2300 Parkway Blvd": 7,  # Deker Lake
    "233 Canyon Rd": 8,  # Salt Lake City Ottinger Hall
    "2530 S 500 E": 9,  # Columbus Library
    "2600 Taylorsville Blvd": 10,  # Taylorsville City Hall
    "2835 Main St": 11,  # South Salt Lake Police
    "300 State St": 12,  # Council Hall
    "3060 Lester St": 13,  # Redwood Park
    "3148 S 1100 W": 14,  # Salt Lake County Mental Health
    "3365 S 900 W": 15,  # Salt Lake County/United Police Dept
    "3575 W Valley Central Station bus Loop": 16,  # West Valley Prosecutor
    "3595 Main St": 17,  # Housing Auth. of Salt Lake County
    "380 W 2880 S": 18,  # Utah DMV Administrative Office
    "410 S State St": 19,  # Third District Juvenile Court
    "4300 S 1300 E": 20,  # Cottonwood Regional Softball Complex
    "4580 S 2300 E": 21,  # Holiday City Office
    "5025 State St": 22,  # Murray City Museum
    "5100 South 2700 West": 23,  # Valley Regional Softball Complex
    "5383 South 900 East #104": 24,  # City Center of Rock Springs
    "600 E 900 South": 25,  # Rice Terrace Pavilion Park
    "6351 South 900 East": 26   # Wheeler Historic Farm
}
# maps all addresses to and index for use with the distance matrix

package_hash = HashMap()
# creates a hash map object

packages = load_packages('cleaned_package_file.csv', address_to_index)
# creates a list of package objects

for package in packages:
    package_hash.add(package.package_id, package.address, package.deadline, package.city, package.zip_code, package.weight, package.status)
# adds all packages to the hash table for quick look up

# create trucks
truck1 = Truck()
truck2 = Truck()

def load_truck1_first_run():
    print("Loading truck #1 for first run:")
    for package_id in [15, 14, 19, 16, 13, 20, 1, 29, 30, 31, 34, 37, 40]:
        package = None
        for p in packages:
            if p.package_id == package_id:
                package = p
                break
        if package and truck1.load_package(package):
            print(f"TRUCK1.ADD({package_id})")
        else:
            print(f"Failed to load package {package_id} onto Truck 1")
# goes through a list of package ids and if they are in the packages list they are added to truck 1

def load_truck2_first_run():
    print("\nLoading truck #2 for first run:")
    for package_id in [3, 18, 36, 38, 2, 4, 5, 7, 8, 10, 11, 12]:
        package = None
        for p in packages:
            if p.package_id == package_id:
                package = p
                break
        if package and truck2.load_package(package):
            print(f"TRUCK2.ADD({package_id})")
        else:
            print(f"Failed to load package {package_id} onto Truck 2")
# goes through a list of package ids and if they are in the packages list they are added to truck 2

def load_truck1_second_run():
    print("\nLoading truck #1 for second run:")
    for package_id in [6, 25, 28, 32, 9]:
        package = None
        for p in packages:
            if p.package_id == package_id:
                package = p
                break
        if package and truck1.load_package(package):
            print(f"TRUCK1.ADD({package_id})")
        else:
            print(f"Failed to load package {package_id} onto Truck 1")
# goes through a list of package ids and if they are in the packages list they are added to truck 1


def load_truck2_second_run():
    print("\nLoading truck #2 second run:") 
    for package_id in [17, 21, 22, 23, 24, 26, 27, 33, 35, 39]:
        package = None
        for p in packages:
            if p.package_id == package_id:
                package = p
                break
        if package and truck2.load_package(package):
            print(f"TRUCK2.ADD({package_id})")
        else:
            print(f"Failed to load package {package_id} onto Truck 2")
# goes through a list of package ids and if they are in the packages list they are added to truck 2

load_truck1_first_run()
load_truck2_first_run()

print("\nTruck #1 status:")
print(truck1)

print("\nTruck #2 status:")
print(truck2)

print("\nStarting deliveries for truck #1 first run:")
truck1.deliver_packages()

print("\nStarting deliveries for truck #2 fist run:")
truck2.deliver_packages()

truck1.time = 9 * 60 + 5  # Set time to 9:05 AM

# Prepare second runs
second_run_packages_truck1 = []
second_run_packages_truck2 = []

for package in packages:
    if package.package_id in [6, 25, 28, 32, 9]:
        second_run_packages_truck1.append(package)
    elif package.package_id in [17, 21, 22, 23, 24, 26, 27, 33, 35, 39]:
        second_run_packages_truck2.append(package)

# Start second run for Truck 1
print("\nStarting second run for truck #1:")
truck1.start_second_run(second_run_packages_truck1)

# Start second run for Truck 2
print("\nStarting second run for truck #2:")
truck2.start_second_run(second_run_packages_truck2)

print("\nFinal truck #1 status:")
print(truck1)

print("\nFinal truck #2 status:")
print(truck2)

# Calculate and print total mileage
total_mileage = truck1.mileage + truck2.mileage
print(f"\nTotal mileage for all trucks: {total_mileage:.1f}")

# Print information for all packages
print("\nAll package info:")
for package in packages:
    print(f"Package {package.package_id}: {package.address}")
    print(package.get_info())
    print()

# Start the user interface
ui = UserInterface([truck1, truck2], packages)
ui.run()