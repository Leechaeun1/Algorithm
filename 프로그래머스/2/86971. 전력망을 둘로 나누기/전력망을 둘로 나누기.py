def dfs(node,graph,visited,is_connected):
    count=1
    visited[node]=True
    
    for neighbor in graph[node]:
        if not visited[neighbor] and is_connected[node][neighbor]:
            count+=dfs(neighbor,graph,visited,is_connected)
    return count

def solution(n, wires):
    min_diff=float('inf')
    
    is_connected=[[True]*(n+1) for _ in range(n+1)]
    
    graph=[[] for _ in range(n+1)]
    
    for u,v in wires:
        graph[u].append(v)
        graph[v].append(u)
        
    for u,v in wires:
        visited=[False]*(n+1)
        
        is_connected[u][v]=False
        is_connected[v][u]=False
        
        count_a=dfs(u,graph,visited,is_connected)
        count_b=dfs(v,graph,visited,is_connected)
        
        is_connected[u][v]=True
        is_connected[v][u]=True
        
        min_diff=min(min_diff,abs(count_a-count_b))
    
    return min_diff