from car import Car


my_new_car = Car('BMW','X5',2016)

print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.update_odometer(44)
my_new_car.update_odometer(50)

my_new_car.read_odometer()

my_new_car.fill_gas_tank()