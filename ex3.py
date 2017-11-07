# cars = 100
# space_in_a_car = 4
# drivers = 30
# passengers = 90
# cars_not_driven = cars - drivers
# cars_driven = drivers
# carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car = passengers / cars_driven
#
# print("There are ", cars, " car available.")
# print("There are onle ", drivers, " drivers available.")
# print("There will be ", cars_not_driven, " empty cars today.")
# print("We can trasport ", carpool_capacity, " people today.")
# print("We have ", passengers, " to carpool today.")
# print("We have to put about ", average_passengers_per_car, " in each car.")

cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are ", cars, " car available.")
print("There are onle ", drivers, " drivers available.")
print("There will be ", cars - drivers, " empty cars today.")
print("We can trasport ", cars_driven * space_in_a_car, " people today.")
print("We have ", passengers, " to carpool today.")
print("We have to put about ", passengers / cars_driven, " in each car.")
