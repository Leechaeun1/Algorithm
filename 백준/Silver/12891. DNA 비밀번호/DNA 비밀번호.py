import sys

s, p = map(int, sys.stdin.readline().split())
dna = sys.stdin.readline().strip()  # strip() 필수
a, c, g, t = map(int, sys.stdin.readline().split())
count = 0

# 문자 카운트 초기화
window_count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for i in range(p):
    window_count[dna[i]] += 1

# 첫 윈도우 검사
if window_count['A'] >= a and window_count['C'] >= c and window_count['G'] >= g and window_count['T'] >= t:
    count += 1

# 슬라이딩 윈도우
for i in range(p, s):
    out_ch = dna[i - p]
    in_ch = dna[i]
    window_count[out_ch] -= 1
    window_count[in_ch] += 1

    if window_count['A'] >= a and window_count['C'] >= c and window_count['G'] >= g and window_count['T'] >= t:
        count += 1

print(count)
