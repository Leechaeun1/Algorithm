import sys
from queue import PriorityQueue

n = int(sys.stdin.readline())
q = PriorityQueue()

for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if q.empty():
            print(0)
        else:
            q1 = q.get()
            print(str(q1[1]))
    else:
        q.put((abs(x), x))
