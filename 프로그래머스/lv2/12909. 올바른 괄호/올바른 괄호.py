def solution(s):
    stack = []
    for i in s:
        try:
            if i == '(':
                stack.append(i)
            else:
                stack.pop()
        except:
            return False

    if len(stack) == 0:
        return True
    else:
        return False