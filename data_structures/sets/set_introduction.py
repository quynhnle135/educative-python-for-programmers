my_set = {"Educative", 1, 2, 3, (True, False)}
print(my_set)
print(len(my_set))

random_set = set({"Educative", 1, 2, 3, (True, False)})
print(random_set)

random_set.add("Quinn")
print(random_set)
random_set.update([7, 8, 9, 10])
print(random_set)
random_set.remove("Educative")
print(random_set)
random_set.discard("Quinn")
print(random_set)