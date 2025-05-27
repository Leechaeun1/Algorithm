def dfs(node, graph, visited, is_connected):
    count = 1
    visited[node] = True

    for neighbor in graph[node]:
        # 아직 방문하지 않았고, 해당 간선이 끊어지지 않은 경우
        if not visited[neighbor] and is_connected[node][neighbor]:
            count += dfs(neighbor, graph, visited, is_connected)

    return count


def solution(n, wires):
    min_diff = float('inf')

    # 각 노드 간 연결 여부를 나타내는 2차원 배열
    is_connected = [[True] * (n + 1) for _ in range(n + 1)]

    # 그래프 인접 리스트 초기화
    graph = [[] for _ in range(n + 1)]

    # 그래프 구성
    for u, v in wires:
        graph[u].append(v)
        graph[v].append(u)

    # 모든 간선을 하나씩 끊어보면서 두 전력망의 노드 수 차이 계산
    for u, v in wires:
        visited = [False] * (n + 1)

        # 간선 끊기
        is_connected[u][v] = False
        is_connected[v][u] = False

        # 각각의 전력망 노드 수 세기
        count_a = dfs(u, graph, visited, is_connected)
        count_b = dfs(v, graph, visited, is_connected)

        # 간선 다시 복구
        is_connected[u][v] = True
        is_connected[v][u] = True

        # 최소 차이값 갱신
        min_diff = min(min_diff, abs(count_a - count_b))

    return min_diff
