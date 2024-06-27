def romanToInt(numeral):
    """
    :type s: str
    :rtype: int
    """
    mapping = {
        "I": 1, 
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = 0
    for i in range(len(numeral) - 1):
        val = mapping[numeral[i]]
        next_val = mapping[numeral[i + 1]]

        if val < next_val:
            result -= val
        else:
            result += val
    result += mapping[numeral[len(numeral) - 1]]
    return result