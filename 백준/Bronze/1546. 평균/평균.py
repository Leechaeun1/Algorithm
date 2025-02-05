n = int(input())
li = list(map(int, input().split())) # 리스트 입력 시 한 줄로 입력

m = max(li)
for i in range(n):
    li[i] = li[i] / m * 100

avg = sum(li) / n
print(avg)