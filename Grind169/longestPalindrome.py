def longestPalindrome(s):
    hash_map1 = {}

    for i in range(len(s)):
        if s[i] not in hash_map1:
            hash_map1[s[i]] = 0
        hash_map1[s[i]] += 1
    counter = 0
    for i in hash_map1.keys():
        if hash_map1[i] % 2 == 0:
            counter += hash_map1[i]
    odds = []
    for i in hash_map1.keys():
        if hash_map1[i] % 2 != 0:
            odds.append(hash_map1[i])
    for val in odds:
        counter += val - 1
    if odds == []:
        return counter
    return counter + 1
            
        
    
