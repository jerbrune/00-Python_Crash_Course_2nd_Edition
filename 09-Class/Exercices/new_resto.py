from resturant import *

mon_resto=Restaurant('le dulcis','francaise')
mon_resto.describe_restaurant()
mon_resto.open_restaurant()

print(mon_resto.number_served)
mon_resto.number_served=10
print(mon_resto.number_served)

mon_resto.set_number_served(40)

glace = IceCreamStand('miko','glacier',['fraise','chocolat','vanille'])
print(glace.flavor)
glace.flavor_list()