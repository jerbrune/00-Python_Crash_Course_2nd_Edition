class Car:
    """A simple attempt to represent a car."""

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f'This car has {self.odometer_reading} km on it')

    def update_odometer(self,km):
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print("il n'est pas possible de diminuer le nombre de km")
    
    def increment_odometer(self,km):
        self.odometer_reading += km

    def fill_gas_tank(self):
        print("gazole")

class Battery:
    def __init__(self,battery_size=75):
        self.battery_size = battery_size
    
    def decribe_battery(self):
        print (f"This cas has a {self.battery_size} - kWh battery.")

class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make,model,year)
        #self.battery_size = 75
        self.battery = Battery()
    
    #def describe_baterry(self):
    #    print(f"This car has a {self.battery_size} - KWh battery.")
    
    #def fill_gas_tank(self):
    #    print("this car doesn't need a gas tank !")


