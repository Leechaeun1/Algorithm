import copy

INF = int(1e9)

# 노드, 간선
n, m = map(int, input().split())

# 인접 행렬
graph = [[INF] * n for _ in range(n)]

# 나 -> 나 거리는 0
for i in range(n):
    graph[i][i] = 0

# 관계 입력이니까 m번(간선 수) 반복
for _ in range(m):
    # 친구 관계는 양방향으로
    a, b = map(int, input().split())
    # 리스트 인덱스는 0부터 시작인데 입력번호는 1부터 시작하니까 1 빼주기
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1


def floyd():
    d = copy.deepcopy(graph)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
    return d


dist = floyd()

# 최소값 저장 변수
result = 0
# 케빈 베이컨 수가 가장 작은 사람 저장
person = 0

for i in range(n):
    # i번째 사람과 모든 사람 간의 최단 거리를 합산
    total = sum(dist[i])
    if result == 0 or total < result:
        result = total
        # 파이썬 인덱스가 0부터 시작하니까 +1
        person = i + 1

print(person)
