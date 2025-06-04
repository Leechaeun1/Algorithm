# n : 집합 S에 포함되어 있는 문자열 갯수
# m : 검사해야 하는 문자열 갯수
n, m = map(int, input().split())
# set 사용한 문자열 저장할 집합 S (리스트보다 검색속도 빠름)
s = set()
# 출력 변수
count = 0

# n개의 문자열 입력 받고 s에 추가
for _ in range(n):
    s.add(input())

# 1. m개의 문자열 입력 받고 
for i in range(m):
    # 2. 집합 S에 있으면 count += 1
    if input() in s:
        count += 1
        
print(count)
