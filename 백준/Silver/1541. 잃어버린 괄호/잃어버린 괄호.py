n = input().split('-')
num = []

for i in n:
    cnt=0
    for j in i.split('+'):
        cnt += int(j)
    num.append(cnt)
result = num[0]
for i in num[1:]:
    result -= i
print(result)
