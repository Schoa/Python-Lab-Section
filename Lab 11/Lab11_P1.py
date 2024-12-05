class Car:
    def __init__(self, speed, consumption_rate, fuel_level):
        self.speed = speed  # Speed of the car (km/h)
        self.consumption_rate = consumption_rate  # Fuel consumption rate (units/hour)
        self.fuel_level = fuel_level  # Current fuel level (units)

    def can_reach(self, distance):
        # Calculate the maximum distance the car can travel with the current fuel level
        max_distance = (self.fuel_level / self.consumption_rate) * self.speed
        return max_distance >= distance  # Return True if it can reach, False otherwise

    def refuel_cost(self, price_per_unit):
        # Calculate cost to refuel to 100 fuel level
        return (100 - self.fuel_level) * price_per_unit


# Input
input_data = input()
speed, consumption_rate, fuel_level, distance, price_per_unit = map(int, input_data.split())

# Create a Car object
my_car = Car(speed, consumption_rate, fuel_level)

# Output the car's attributes
print(my_car.speed, my_car.consumption_rate, my_car.fuel_level)

# Check if the car can reach the given distance
print(my_car.can_reach(distance))

# Calculate and print the refuel cost
print(my_car.refuel_cost(price_per_unit))