import car

my_tesla = car.ElectricCar('Tesla','model s','2019')
print(my_tesla.get_descriptive_name())
#my_tesla.describe_baterry()
my_tesla.fill_gas_tank()
my_tesla.battery=car.Battery(80)
my_tesla.battery.decribe_battery()
