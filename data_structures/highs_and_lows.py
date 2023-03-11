def count_highs_and_lows(nums_list):
    lows = 0
    highs = 0
    for n in nums_list:
        if n > 50 or n % 3 == 0:
            highs += 1
        else:
            lows += 1
    return [lows, highs]


nums_list = [20, 9, 51, 81, 50, 42, 77]
print(count_highs_and_lows(nums_list))
