def slidingWindow(s, k): 
    windowStart = 0
    maximum = 0
    char_freq = {}
    for windowEnd in range(len(s)):
        right_char = s[windowEnd]
        if right_char not in char_freq: 
            char_freq[right_char] = 0
        char_freq[right_char] += 1

        while len(char_freq) > k:
            left_char = s[windowStart]
            char_freq[left_char] -= 1
            if char_freq[left_char] == 0:
                del char_freq[left_char]
            windowStart += 1
        maximum = max(maximum, windowEnd - windowStart + 1)
    return maximum
        

print(slidingWindow([1,2,3,3,2,6,7,1], 3))