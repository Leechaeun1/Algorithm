from collections import deque
import sys

n, m, start = map(int, sys.stdin.readline().split())
# 인접 리스트 생성
graph = [[] for _ in range(n + 1)]

# 간선 정보 입력
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    # 인접 리스트
    # 무방향 그래프이므로 a에서 b로 갈 수 있다면, b에서 a로도 갈 수 있어야 한다
    # graph[a] : 정점 a에 연결된 이웃들을 저장하는 리스트
    # .append(b) : 그 리스트에 정점 b를 추가
    # a번째 정점에 b연결
    graph[a].append(b)
    # b번째 정점에 a연결
    graph[b].append(a)

# 정점 번호가 작은 순서부터 탐색해야 하므로 sort() 사용
# 정점 번호가 1부터 시작하기 때문데 범위가 1부터 n+1
# graph[0]은 "더미공간"
for i in range(1, n + 1):
    graph[i].sort()

visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)


# dfs 함수 (재귀)
def dfs(v):
    visited_dfs[v] = True
    print(v, end=' ')

    for i in graph[v]:
        # 만약 i 값을 방문하지 않았고 v와 연결이 되어있다면
        if not visited_dfs[i]:
            # 해당 i 값으로 dfs 호출
            dfs(i)


# bfs 함수 (큐)
def bfs(v):
    queue = deque([v])
    visited_bfs[v] = True
    print(v, end=' ')

    while queue:
        current = queue.popleft()

        for i in graph[current]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True
                print(i, end=' ')


dfs(start)
print()
bfs(start)
