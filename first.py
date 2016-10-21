cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_nit_driven = cars-drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passenger_per_car = passengers / cars_driven

newstring="There are "+ str(cars) + "cars available"
print(newstring)
print("tHere are",cars,"cars available",sep="-")
values=(cars,"cars")
f= "there are %d %s available" % values
f= "there are %d %s available"(cars,"cars")
