def multiplier(n):
    return lambda x: x * n

result = multiplier(2)

print(result(15))