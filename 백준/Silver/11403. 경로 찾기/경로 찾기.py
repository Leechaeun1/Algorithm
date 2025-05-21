import copy
# 노드(정점)의 개수
n = int(input())

# 입력 그래프: 인접 행렬로 표현
graph=[]
for _ in range(n):
    row = list(map(int,input().split()))
    graph.append(row)


def floyd_warshall():
    # 결과 그래프 초기화: 입력 그래프를 그대로 복사하여 사용
    # d[i][j]는 i번 노드에서 j번 노드까지의 최단 거리 정보를 저장
    d = copy.deepcopy(graph)

    # Floyd-Warshall 알고리즘 수행
    for k in range(n):            # k: 거쳐가는 노드
        for i in range(n):        # i: 출발 노드
            for j in range(n):    # j: 도착 노드
                # 만약 i -> k -> j 경로가 존재 한다면 1
                if d[i][k] == 1 and d[k][j] == 1:
                    d[i][j] = 1

    # 최종 결과 출력
    for i in range(n):
        for j in range(n):
            print(d[i][j], end=" ")
        print()  # 행 끝 줄바꿈

# 메인 함수: 알고리즘 실행
floyd_warshall()
