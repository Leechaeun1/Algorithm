import heapq
def solution(n, paths, gates, summits):
    g=[[]for _ in range(n+1)];[g[i].append((j,w)) or g[j].append((i,w)) for i,j,w in paths]
    m=[float('inf')]*(n+1);pq=[];[heapq.heappush(pq,(0,gt)) or m.__setitem__(gt,0) for gt in gates]
    s=set(summits)
    while pq:
        i,u=heapq.heappop(pq)
        if i>m[u] or u in s:continue
        for v,w in g[u]:
            ni=max(i,w)
            if ni<m[v]:m[v]=ni;heapq.heappush(pq,(ni,v))
    a=[-1,float('inf')];summits.sort()
    for sx in summits:
        if m[sx]<a[1]:a[0],a[1]=sx,m[sx]
    return a