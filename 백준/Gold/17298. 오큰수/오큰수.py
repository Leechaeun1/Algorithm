import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
result = [-1] * n # -1을 디폴트로 설정
stack = []
for i in range(n):
    # 현재 값이 top보다 크면 오큰수
    while stack and a[stack[-1]] < a[i]:
        idx = stack.pop()
        result[idx] = a[i] # 오큰수로 현재 값 설정
    stack.append(i)

print(*result)
