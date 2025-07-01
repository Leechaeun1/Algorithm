def to_sec(t): return int(t[:2]) * 3600 + int(t[3:5]) * 60 + int(t[6:])
def to_str(s): return f'{s//3600:02}:{s%3600//60:02}:{s%60:02}'

def solution(play_time, adv_time, logs):
    p, a = to_sec(play_time), to_sec(adv_time)
    times = [0] * (p + 2)
    
    for log in logs:
        s, e = map(to_sec, log.split('-'))
        times[s] += 1
        times[e] -= 1

    for i in range(1, p + 1): times[i] += times[i - 1]
    for i in range(1, p + 1): times[i] += times[i - 1]

    max_time, max_view = 0, times[a - 1]
    for i in range(a, p):
        cur = times[i] - times[i - a]
        if cur > max_view:
            max_view, max_time = cur, i - a + 1

    return to_str(max_time)
