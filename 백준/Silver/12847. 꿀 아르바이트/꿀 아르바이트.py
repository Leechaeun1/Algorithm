n, m = map(int, input().split())
t = list(map(int, input().split()))
current_sum = sum(t[:m])
max_sum = current_sum

for i in range(1, n - m + 1):
    current_sum = current_sum - t[i - 1] + t[i + m - 1]

    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)