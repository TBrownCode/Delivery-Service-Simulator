import datetime

class UserInterface:
    def __init__(self, trucks, packages):
        self.trucks = trucks
        self.packages = packages

    def run(self):
        while True:
            print("\nWGUPS Package Tracker")
            print("1. Check status of a package")
            print("2. Check status of all packages")
            print("3. Check status of all packages at a specific time")
            print("4. View truck status and total mileage")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                self.check_package_status()
            elif choice == '2':
                self.check_all_packages()
            elif choice == '3':
                self.check_status_at_time()
            elif choice == '4':
                self.view_truck_status()
            elif choice == '5':
                print("Exited - Thanks for using WGUPS Package Tracker")
                break
            else:
                print("Invalid choice. Please try again.")
    # runs the main menu loop

    def check_package_status(self):
        package_id = input("Enter package ID: ")
        try:
            package_id = int(package_id)
            package = None
            for p in self.packages:
                if p.package_id == package_id:
                    package = p
                    break
            if package:
                print(f"\nPackage {package_id} Status:")
                status, time = self.get_package_status_with_time(package)
                print(f"Status: {status} at {time}")
                print(package.get_info())
            else:
                print(f"Package with ID {package_id} not found.")
        except ValueError:
            print("Invalid package ID. Please enter a number.")
    # checks the status of a specific package

    def check_all_packages(self):
        print("\nStatus of All Packages:")
        for package in self.packages:
            status, time = self.get_package_status_with_time(package)
            print(f"Package {package.package_id}: {status} at {time}")
    # checks the status of all packages

    def check_status_at_time(self):
        time_str = input("Enter time (HH:MM): ")
        try:
            check_time = datetime.datetime.strptime(time_str, "%H:%M").time()
            print(f"\nStatus of All Packages at {time_str}:")
            for package in self.packages:
                status = self.get_package_status_at_time(package, check_time)
                print(f"Package {package.package_id}: {status}")
        except ValueError:
            print("Invalid time format. Please use HH:MM.")
    # checks the status of all packages at a specific time
    
    def get_package_status_with_time(self, package):
        if package.delivery_time:
            return "Delivered", package.delivery_time
        elif package.status == "En route":
            return "En route", "08:00" if package.status == "En route" else "Not loaded"
        else:
            return "At hub", "08:00"
    # gets the status and time of a package
    

    def get_package_status_at_time(self, package, check_time):
        if package.delivery_time:
            delivery_time = datetime.datetime.strptime(package.delivery_time, "%H:%M").time()
            if check_time < delivery_time:
                return f"En route at {check_time.strftime('%H:%M')}"
            else:
                return f"Delivered at {package.delivery_time}"
        elif package.status == "En route":
            return f"En route at {check_time.strftime('%H:%M')}"
        else:
            return f"At hub at {check_time.strftime('%H:%M')}"
    # gets the status of a package at a specific time

    def view_truck_status(self):
        total_mileage = sum(truck.mileage for truck in self.trucks)
        print(f"\nTotal mileage for all trucks: {total_mileage:.1f}")
        for i, truck in enumerate(self.trucks, 1):
            print(f"\nTruck {i} Status:")
            print(f"Current Location: {truck.current_location}")
            print(f"Mileage: {truck.mileage:.1f}")
            print(f"Time: {truck.get_current_time()}")
            print("Packages:", ", ".join([str(p.package_id) for p in truck.packages]))
    # gets the status of all trucks and total mileage