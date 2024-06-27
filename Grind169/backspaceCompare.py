def backspaceCompare(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    stack1 = []
    stack2 = []
    for i in s:
        if i == '#':
            if len(stack1) < 1:
                continue 
            stack1.pop()
        else:
            stack1.append(i)
    
    for j in t:
        if j == '#': 
            if len(stack2) < 1:
                continue 
            stack2.pop()
        else:
            stack2.append(j)
    return stack1 == stack2