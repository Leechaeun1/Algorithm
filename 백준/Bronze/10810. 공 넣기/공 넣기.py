n, m = map(int, input().split())
box = [0]*n #0으로 초기화, 공이 없는 바구니는 0 출력해야 하므로
for _ in range(m):
    i, j, k = map(int, input().split())
    for x in range(i-1, j):
        box[x] = k
for i in range(0, n):
    print(box[i], end=" ")