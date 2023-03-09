# adding elements
my_list = [1, 2, 3]
my_list.append("quinn")
print(my_list)

# insert
my_list.insert(2, "Gym")
print(my_list)
my_list.insert(-1, "another value")
my_list.insert(6, "new jeans")

# change element's value
my_list[0] = "Telefono"
print(my_list)

# remove elements
my_list.pop()
print("My list after popping: ", end=" ")
print(my_list)

my_list.remove("Gym")
print(my_list)

# list slicing
another_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(another_list[2: 5])
print(another_list[::2])
print(another_list[::-1])

# search index
cities = ["London", "Paris", "Los Angeles", "Beirut"]
print(cities.index("Beirut"))
print("Vietnam" in cities)
print("Los Angeles" in cities)

# list sort
new_list = [6, 1, 3, 5, 2, 9, 11, 8]
new_list.sort()
print(new_list)