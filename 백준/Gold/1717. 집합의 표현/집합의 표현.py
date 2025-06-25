import sys
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())

parent = [i for i in range(n + 1)]

def union(a, b):
    parent_a = find(a)
    parent_b = find(b)
    parent[parent_a] = parent_b

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

for _ in range(m):
    q, a, b = map(int, input().split())

    if q == 0:  # union
        union(a, b)
    else:  # find
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
