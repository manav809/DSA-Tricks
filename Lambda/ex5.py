nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_nums = filter(lambda x: x % 2 == 0, nums)

print(even_nums)

odd_nums = filter(lambda x: x % 2 != 0, nums)

print(odd_nums)