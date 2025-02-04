n, m = map(int, input().split())
li = list(range(1,n+1))
result = []
for _ in range(m):
    i, j = map(int, input().split())
    li = li[:i-1]+li[i-1:j:][::-1]+li[j:]
print(*li)