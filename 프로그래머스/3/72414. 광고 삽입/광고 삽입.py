# 광고 삽입
def solution(p, a, l):
    T = lambda x: int(x[:2]) * 3600 + int(x[3:5]) * 60 + int(x[6:])

    R = lambda x: f'{x // 3600:02}:{x % 3600 // 60:02}:{x % 60:02}'

    P, A = T(p), T(a)

    t = [0] * (P + 2)

    for log in l:
        s, e = map(T, log.split('-'))
        t[s] += 1
        t[e] -= 1

    for i in range(1, P + 1):
        t[i] += t[i - 1]
    for i in range(1, P + 1):
        t[i] += t[i - 1]

    m, x = t[A - 1], 0
    
    for i in range(A, P):
        v = t[i] - t[i - A]
        if v > m:
            m, x = v, i - A + 1
            
    return R(x)
