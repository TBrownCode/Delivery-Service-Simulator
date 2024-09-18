class Package:

    
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, special_notes, location_index):
        self.package_id = int(package_id)
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = float(weight)
        self.special_notes = special_notes
        self.status = "At hub"
        self.delivery_time = None
        self.location_index = int(location_index)
        # intitialzie our package objects with attributes

    def __str__(self):
        return f"Package {self.package_id}: {self.address}, {self.city}, {self.state} {self.zip_code}"
    # a string representation of our package
    
    def get_info(self):
        return {
            "Package ID": self.package_id,
            "Address": self.address,
            "City": self.city,
            "State": self.state,
            "Zip": self.zip_code,
            "Deadline": self.deadline,
            "Weight": self.weight,
            "Special Notes": self.special_notes,
            "Status": self.status,
            "Delivery Time": self.delivery_time
        }
    # gets info about our packge as a dictionary

    def update_status(self, new_status):
        self.status = new_status
    # updates the status of our package

    def set_delivery_time(self, time):
        self.delivery_time = time
        self.status = "Delivered"
    # sets the status of a package to delivered and updates the delivery time
    