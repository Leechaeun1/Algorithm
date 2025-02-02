from collections import deque

n, k = map(int, input().split())
result=[]
dq = deque(range(1, n+1)) 
while dq:
    dq.rotate(-(k-1)) 
    result.append(dq.popleft()) 
print(str(result).replace('[','<').replace(']','>'))
