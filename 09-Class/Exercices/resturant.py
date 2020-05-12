class Restaurant:
    def __init__(self, restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"le nom du restaurant est {self.restaurant_name}\nSa cuisine est du type {self.cuisine_type}")

    def open_restaurant(self):
        print(f'{self.restaurant_name} est ouvert')

    def set_number_served(self,number):
        self.number_served = number
        print ("le nombre de client servit est de {}".format(self.number_served))
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name,cuisine_type,flavor):
        super().__init__(restaurant_name,cuisine_type)
        self.flavor = flavor
    def flavor_list(self):
        print('les parfums sont :')
        for f in self.flavor:
            print(f"\t{f}")






