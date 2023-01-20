def find_kth_max(lst, k):
    lst.sort()
    return lst[-k]

test_list = [40, 35, 82, 14, 22, 66, 33]
k = 2
print(find_kth_max(test_list, k))