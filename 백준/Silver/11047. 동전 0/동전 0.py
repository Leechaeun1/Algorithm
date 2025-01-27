n, k = map(int, input().split())
coins=[]
cnt = 0

for _ in range (n):
    a = int(input())
    coins.append(a)
coins.sort(reverse=True)


for coin in coins:
    if coin > k :
        continue
    cnt += k // coin #현재 동전으로 사용가능한 최대개수
    k %= coin # 잔액 업데이트
print(cnt)
