n = int(input())
c = []
sum = 0
for _ in range(n):
    a = int(input())
    c.append(a)
c.sort(reverse=True)


for i in range(n):
    if (i+1) % 3 == 0:
        continue
    else:
        sum += c[i]
print(sum)