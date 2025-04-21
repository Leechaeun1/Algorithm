n = int(input())
li = [int(input()) for _ in range(n)]

stack = []
result = []
i = 0

for x in range(1, n + 1):
    stack.append(x)
    result.append('+')

    while stack and stack[-1] == li[i]:
        stack.pop()
        result.append('-')
        i += 1 # 다음 숫자 비교

if stack:
    print('NO')  # stack에 요소 존재 => 수열을 끝까지 만들지 x
else:
    for r in result:
        print(r)
