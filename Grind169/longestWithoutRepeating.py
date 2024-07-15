def lengthOfLongestSubstring(s):
    windowStart = 0
    hash_map = {}
    longest = 0
    for windowEnd in range(len(s)):
        right_char = s[windowEnd]
        if right_char not in hash_map:
            hash_map[right_char] = 0
        hash_map[right_char] += 1

        while hash_map[right_char] > 1:
            left_char = s[windowStart]
            hash_map[left_char] -= 1
            if hash_map[left_char] == 0:
                del hash_map[left_char]
            windowStart += 1
        
        longest = max(longest, windowEnd - windowStart + 1)
    return longest