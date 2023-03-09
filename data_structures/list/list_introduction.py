my_list = ["Quinn", "Verity", 22, {"author": "coho"}]

print("My whole list: ", end=" ")
print(my_list)

print("Print my list but step 2 steps at once: ", end=" ")
print(my_list[::2])

print("Print my list backwards: ", end=" ")
print(my_list[::-1])

print("Get the dict value in my list: ", end=" ")
print(my_list[-1]["author"])

print("Even numbers: ", end= " ")
for i in range (0, 11):
    if i % 2 == 0:
        print(i, end= " ")

