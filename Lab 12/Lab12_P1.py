class Vehicle:
    def __init__(self, brand, model, year):
        """Constructor to initialize the attributes of the vehicle."""
        self.brand = brand  # The brand of the vehicle
        self.model = model  # The model of the vehicle
        self.year = year    # The manufacturing year of the vehicle

    def display_info(self):
        """Returns the vehicle's information."""
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"

class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        """Constructor to initialize the attributes of the car."""
        super().__init__(brand, model, year)  # Call the constructor of the base class
        self.num_doors = num_doors  # The number of doors in the car

    def display_info(self):
        """Returns the vehicle's information along with the number of doors."""
        base_info = super().display_info()  # Get info from Vehicle class
        return f"{base_info}, Number of doors: {self.num_doors}"

class Truck(Vehicle):
    def __init__(self, brand, model, year, payload_capacity):
        """Constructor to initialize the attributes of the truck."""
        super().__init__(brand, model, year)  # Call the constructor of the base class
        self.payload_capacity = payload_capacity  # The payload capacity of the truck

    def display_info(self):
        """Returns the vehicle's information along with the payload capacity."""
        base_info = super().display_info()  # Get info from Vehicle class
        return f"{base_info}, Payload Capacity: {self.payload_capacity}"

n = int(input())  # Read number of vehicles
vehicles = []  # List to store vehicle instances

for _ in range(n):
    details = input().split()  # Read vehicle details
    vehicle_type = details[0]  # First word indicates type (Car or Truck)

    if vehicle_type == "Car":
        # Unpack details for Car
        _, brand, model, year, num_doors = details
        vehicles.append(Car(brand, model, int(year), int(num_doors)))
    
    elif vehicle_type == "Truck":
        # Unpack details for Truck
        _, brand, model, year, payload_capacity = details
        vehicles.append(Truck(brand, model, int(year), float(payload_capacity)))

# Display information for each vehicle
for vehicle in vehicles:
    print(vehicle.display_info())