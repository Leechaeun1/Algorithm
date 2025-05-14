import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
# 이분 그래프 여부 저장
IsEven = True

def dfs(node):
    global IsEven
    # 현재 노드 방문 처리
    visited[node] = True

    for i in graph[node]:
        if not visited[i]:
            # 인접 노드는 같은 집합이 아니므로 다른 집합으로 처리
            check[i] = (check[node] + 1) % 2
            dfs(i)
        # 이미 방문한 노드가 현재 내 노드와 같은 집합이면 이분 그래프 아님
        elif check[node] == check[i]:
            IsEven = False

# 테스트 케이스만큼 반복
for _ in range(n):
    # 정점 수 v, 간선 수 e
    v, e = map(int, input().split())
    # 그래프 초기화 - 인접 리스트
    graph = [[] for _ in range(v + 1)]

    # 방문 여부 리스트
    visited = [False] * (v + 1)
    # 노드별 집합(그룹 정보) 저장 리스트
    check = [0] * (v + 1)
    # 매 테케마다 초기화
    IsEven = True

    # 간선 정보 입력
    for i in range(e):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)

    # 모든 정점에서 dfs 시작
    for i in range(1, v + 1):
        if IsEven:
            dfs(i)
        else:
            break

    if IsEven:
        print("YES")
    else:
        print("NO")
    