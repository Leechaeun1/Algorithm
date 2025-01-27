import sys


n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
li.sort(reverse=True)

tmp = []
sum_tmp = []

if n % 2 != 0:
    tmp.append(li[0])
    li.remove(li[0])
    n -= 1
    for i in range(n // 2):
        tmp.append([li[i], li[n - i - 1]])
        sum_tmp = [tmp[0]] + [sum(sublist) for sublist in tmp[1:]]
    print(max(sum_tmp))

elif n % 2 == 0:
    for i in range(n // 2):
        tmp.append([li[i], li[n - i - 1]])
        sum_tmp = [sum(sublist) for sublist in tmp]
    print(max(sum_tmp))
