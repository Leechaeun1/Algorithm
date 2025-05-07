N = int(input())
start, end, count, Sum = 1, 1, 0, 1

while end <= N:
    if Sum < N:
        end += 1
        Sum += end
    elif Sum > N:
        Sum -= start
        start += 1
    else:
        count += 1
        end += 1
        Sum += end
print(count)
