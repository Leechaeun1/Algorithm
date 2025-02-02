#큐

import sys
n = int(sys.stdin.readline())
stk = []
for _ in range(n):
    num = sys.stdin.readline().split()

    if num[0] == 'push':
        stk.append(num[1])

    elif num[0] == 'pop':
        if stk:
            print(stk.pop(0))
        else:
            print('-1')

    elif num[0] == 'size':
        print(len(stk))

    elif num[0] == 'empty':
        if not stk:
            print('1')
        else :
            print('0')
    elif num[0] == 'front':
        if stk:
            print(stk[0])
        else:
            print('-1')
    elif num[0] == 'back':
        if stk:
            print(stk[-1])
        else:
            print('-1')