from collections import deque

d = deque()
def solution(s):
    for i in range(len(s)):

        if s[i]=='(':
            d.append(s[i])
        elif s[i]==')':
            if not d:
                return False
            else:
                d.pop()
    if d:
        return False
    return True
