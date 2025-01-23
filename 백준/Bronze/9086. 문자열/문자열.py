t = int(input())
li = []
for _ in range(t):
    li.append(input())
for i in range(t):
    print(f"{li[i][0]}{li[i][-1]}")