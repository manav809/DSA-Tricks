def isPalindrome(s: str) -> bool:
    string = ""
    for char in s:
        if char.isalnum():
            string += char.lower()

    stack = []
    for char in string:
        stack.append(char)
    
    for char in string:
        if char == stack.pop():
            continue
        return False
    return True