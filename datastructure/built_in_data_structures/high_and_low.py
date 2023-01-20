def find_high_and_low(lst):
    high = 0
    low = 0
    for n in lst:
        if n > 50 or n % 3 == 0:
            high += 1
        else:
            low +=1
    return [low, high]


print(find_high_and_low([20, 9, 51, 81, 50, 42, 77]))