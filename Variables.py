cars = 100
space_in_car = 4.0
drivers = 20
passengers = 100
cars_not_driven = cars - drivers
pool_cap = drivers * space_in_car

print "There are ", cars, " cars available."
print "However, there are only", drivers, "cars available, so there will be", cars_not_driven, "empty cars."