import sys
input = sys.stdin.readline
n = int(input())
li = []
for _ in range(n):
    li.append(input().rstrip()) #개행문자 제거

li = list(set(li)) #중복 제거
li.sort()          #사전 순서로 정렬
li.sort(key=len)   #길이순으로 정렬

for i in li:
    print(i)