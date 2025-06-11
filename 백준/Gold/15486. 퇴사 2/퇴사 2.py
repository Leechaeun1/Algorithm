import sys
input = sys.stdin.readline

n = int(input())
arr = []
# t: 기간, p: 금액
for _ in range(n):
    t, p = map(int, input().split())
    arr.append([t, p])

# 수익 리스트
# dp[i] : i ~ n일까지의 최대 수익
dp = [0] * (n + 1)

# 뒤에서부터 계산하기(n-1일부터 0일까쥐)
for i in reversed(range(n)):
    # 선택 1 : 오늘 상담 안하기
    dp[i] = dp[i + 1]

    # 선택 2 : 오늘 상담 하기(상담 끝나는 날이 퇴사일 이내라면)
    if i + arr[i][0] <= n:
        # 현재 상황과 (상담 수익 + 상담 끝난 후 최대 수익) 중 더 큰 값
        dp[i] = max(dp[i], arr[i][1] + dp[i + arr[i][0]])
print(dp[0])