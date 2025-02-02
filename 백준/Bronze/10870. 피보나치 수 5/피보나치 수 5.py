n = int(input())
li = [0,1] + [0]*(n - 1) #리스트를 크기만큼 초기화
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2, n+1):
            li[i] = li[i - 1] + li[i - 2]
        return li[n]

print(fibonacci(n))