from collections import deque
import sys

n = int(sys.stdin.readline())
dq = deque()
for _ in range(n):
    num = sys.stdin.readline().split()

    if num[0] == 'push_front':
        x = int(num[1])
        dq.appendleft(x)
    elif num[0] == 'push_back':
        x = int(num[1])
        dq.append(x)
    elif num[0] == 'pop_front':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif num[0] == 'pop_back':
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif num[0] == 'size':
        print(len(dq))
    elif num[0] == 'empty':
        print(1 if not dq else 0)
    elif num[0] == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif num[0] == 'back':
        if dq:
            print(dq[-1])
        else:
            print(-1)
