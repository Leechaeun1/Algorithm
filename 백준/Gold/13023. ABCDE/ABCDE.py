import sys

sys.setrecursionlimit(10 ** 6)

n, m = map(int, sys.stdin.readline().split())
# 인접 리스트 생성
graph = [[] for _ in range(n + 1)]

# 간선 정보 입력
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 정점 번호가 작은 순서부터 탐색해야 하므로 정렬
for i in range(1, n + 1):
    graph[i].sort()

# 방문 확인 리스트 초기화
visited = [False] * (n + 1)

result = 0

# dfs 함수 (재귀)
def dfs(v, depth):
    global result
    if depth == 4:  # 깊이가 4에 도달하면 결과를 1로 설정하고 종료
        result = 1
        return

    visited[v] = True  # 현재 정점을 방문 처리

    for i in graph[v]:
        if not visited[i]:  # 방문하지 않은 노드만 탐색
            dfs(i, depth + 1)

    visited[v] = False  # 백트래킹: 현재 정점에서 탐색이 끝나면 방문 처리 해제

# 모든 노드에 대해 dfs 실행
for i in range(1, n + 1):
    if result == 1:  # 만약 이미 1을 찾았다면 더 이상 탐색할 필요 없음
        break
    visited = [False] * (n + 1)  # 새로운 시작점에서 방문 정보 초기화
    dfs(i, 0)

print(result)
