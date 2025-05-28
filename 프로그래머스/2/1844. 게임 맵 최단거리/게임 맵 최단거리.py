from collections import deque

def solution(maps):
    rows=len(maps)
    cols=len(maps[0])
    
    queue=deque()
    queue.append((0,0))
    
    dx=[-1,1,0,0]
    dy=[0,0,1,-1]
    
    while queue:
        x,y=queue.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx<0 or nx>=rows or ny<0 or ny>=cols:
                continue
            
            if maps[nx][ny]==1:
                maps[nx][ny]=maps[x][y]+1
                queue.append((nx,ny))
    
    return -1 if maps[rows-1][cols-1]==1 else maps[rows-1][cols-1]