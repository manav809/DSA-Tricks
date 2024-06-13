def canConstruct(ransomNote, magazine):
    hash_map1 = {}

    for i in range(len(ransomNote)):
        char = ransomNote[i]
        if char not in hash_map1:
            hash_map1[char] = 0
        hash_map1[char] += 1
    
    for i in range(len(magazine)):
        char = magazine[i]
        if char in hash_map1:
            hash_map1[char] -= 1
            if hash_map1[char] == 0: del hash_map1[char]
    return len(hash_map1) == 0