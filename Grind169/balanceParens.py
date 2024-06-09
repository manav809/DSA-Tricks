def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    """
    1. Add (, {, [ to stack 
    2. if we get reverse, lets pop out of the stack
    3. if stack is empty return True else False
    """
    stack = []
    for i in range(len(s)):
        if s[i] == "(" or s[i] == "{" or s[i] == "[":
            stack.append(s[i])
        else:
            if len(stack) == 0:
                return False
            x = stack[-1]
            if s[i] == ")":
                if x == "(":
                    stack.pop()
                else: return False
            elif s[i] == "}":
                if x == "{":
                    stack.pop()
                else: return False
            elif s[i] == "]":
                if x == "[":
                    stack.pop()
                else: return False

    if len(stack) == 0:
        return True
    else:
        return False