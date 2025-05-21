import sys
import heapq

input = sys.stdin.readline
INF = int(1e9) # 무한대를 의미

def dijkstra(start, graph, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q) # 최단거리가 가장 짧은 노드 정보 꺼내기

        # 이미 처리된 노드라면 continue
        if distance[now] < dist:
            continue

        for neighbor in graph[now]:
            target_node = neighbor[0] # 도착 노드 번호
            edge_cost = neighbor[1] # 현재 노드 -> target_node까지의 거리
            cost = dist + edge_cost # 시작점 -> 현재 노드까지 거리 + 현재 -> 인접 거리
            # 기존 거리보다 더 짧은 경로가 있다면 갱신
            if cost < distance[target_node]:
                distance[target_node] = cost
                heapq.heappush(q, (cost, target_node))
    return distance # 모든 노드까지의 최단 거리 리스트 반환

# 노드
n = int(input())
# 간선
m = int(input())

# 인접 리스트
graph = [[] for _ in range(n + 1)]

# 그래프 입력
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 시작점, 끝점 입력받기
start, end = map(int, input().split())

# 무한으로 초기화
distance = [INF] * (n + 1)

dijkstra(start, graph, distance)

# 최단 거리 출력
print(distance[end])
