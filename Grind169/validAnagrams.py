def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    hash_map_1 = {}
    hash_map_2 = {}
    for i in range(len(s)):
        if s[i] not in hash_map_1:
            hash_map_1[s[i]] = 0
        hash_map_1[s[i]] += 1
    
    for i in range(len(t)):
        if t[i] not in hash_map_2:
            hash_map_2[t[i]] = 0
        hash_map_2[t[i]] += 1
    return hash_map_1 == hash_map_2
        
