t = int(input())
c_list = []
for _ in range (t):
    c = int(input())
    c_list.append(c)
# c_list = [int(input()) for _ in range(t)]


q = 25
d = 10
n = 5
p = 1

for c in c_list:
    cnt_q = 0
    cnt_d = 0
    cnt_n = 0
    cnt_p = 0

    cnt_q = c // q
    c %= q

    cnt_d = c // d
    c %= d

    cnt_n = c // n
    c %= n

    cnt_p = c // p
    c %= p

    print(cnt_q, cnt_d, cnt_n, cnt_p)