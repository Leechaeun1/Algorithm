n = int(input())
nodelist = list(map(int, input().split()))
erase = int(input())

def dfs(num, nodelist):
    # 삭제 노드와 자식 노드를 모두 삭제 처리
    # -2 : 삭제된 노드를 의미
    nodelist[num] = -2
    for i in range(len(nodelist)):
        if num == nodelist[i]:
            dfs(i, nodelist)

dfs(erase, nodelist)
# count : 리프 노드 개수
count = 0
for i in range(len(nodelist)):
    # 삭제된 노드가 아니고
    # 어느 노드의 부모가 아니라면 count++
    if nodelist[i] != -2 and i not in nodelist:
        count += 1
print(count)
