set_A = {1, 2, 3, 4}
set_B = {"A", "B", "C", "D", 1, 2, 3}

print("Union: ")
print(set_A | set_B)
print(set_A.union(set_B))
print(set_B.union(set_A))

print("Intersection: ")
print(set_A.intersection(set_B))
print(set_B.intersection(set_A))
print(set_A & set_B)

print("Difference: ")
print(set_A - set_B)
print(set_A.difference(set_B))
print(set_B - set_A)
print(set_B.difference(set_A))

my_set = {7, 3, 1, 8, 9, 10}
print(my_set)

traffic_light = {"Green": "Go", "Red": "Stop"}
print(traffic_light.popitem())

