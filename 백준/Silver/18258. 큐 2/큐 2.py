#큐 코드
from collections import deque
import sys
n = int(sys.stdin.readline())
dq = deque()
for _ in range(n):
    num = sys.stdin.readline().split()

    if num[0] == 'push':
        dq.append(num[1])

    elif num[0] == 'pop':
        if dq:
            print(dq.popleft())
        else:
            print('-1')

    elif num[0] == 'size':
        print(len(dq))

    elif num[0] == 'empty':
        if not dq:
            print('1')
        else :
            print('0')
    elif num[0] == 'front':
        if dq:
            print(dq[0])
        else:
            print('-1')
    elif num[0] == 'back':
        if dq:
            print(dq[-1])
        else:
            print('-1')