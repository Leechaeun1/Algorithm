from collections import deque

def solution(maps):
    rows = len(maps)      # 행 (세로 길이)
    cols = len(maps[0])   # 열 (가로 길이)
    
    # BFS를 위한 큐 초기화 (시작점 (0, 0))
    queue = deque()
    queue.append((0, 0))
    
    # 상, 하, 좌, 우 방향 벡터
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    # BFS 수행
    while queue:
        x, y = queue.popleft()

        # 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵 범위를 벗어난 경우 무시
            if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                continue

            # 이동 가능한 칸(1)이면, 현재까지의 거리 누적
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))

    # 도착 지점까지 도달하지 못한 경우 -1, 도달했다면 거리 반환
    return -1 if maps[rows - 1][cols - 1] == 1 else maps[rows - 1][cols - 1]
