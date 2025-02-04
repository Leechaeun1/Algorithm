a, b = map(int, input().split())
c = int(input())

b += c

if b >= 60:
    a += b // 60
    b = b % 60
    if a >= 24:
        a = a+ (b//60)
        #24보다 크면 24미만이 될때까지 계속 24 빼
        a -= 24

    print(a, b)
else:
    print(a, b)