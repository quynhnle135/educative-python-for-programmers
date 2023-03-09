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