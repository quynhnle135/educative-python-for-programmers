nums = [10, 20, 30, 40, 50]
nums_doubled = []

for i in nums:
    nums_doubled.append(i * 2)

print(nums)
print(nums_doubled)

nums_squared = [n ** 2 for n in nums]
print(nums_squared)

even_nums = [n for n in nums if n % 2 == 0 and n % 3 == 0]
print(even_nums)

# multiple lists
list1 = [30, 50, 110, 40, 15, 75]
list2 = [10, 60, 20, 50]

sum_list = [(n1, n2) for n1 in list1 for n2 in list2 if n1 + n2 > 100]
print(sum_list)
new_list = list1 + list2
new_list.sort()
print(new_list)

num_seq = range(0, 11)
num_list = list(num_seq)
print(num_list)

another_num_seq = range(0, 20, 5)
another_num_list = list(another_num_seq)
print(another_num_list)

# list in list
list_in_list = [
        ["my first list", "quinn", "books"],
        ["my second list", "another quin", "many more books"]
    ]

print(list_in_list)
print(list_in_list[0])
print(list_in_list[1][2])

# list extension
part_A = [1, 2, 3, 4, 5]
part_B = [6, 7, 8, 9, 10]
part_A.extend(part_B)
print(part_A)