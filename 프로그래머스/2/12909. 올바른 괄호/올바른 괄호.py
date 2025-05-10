def solution(s):
    stack = []
    # 문자열을 돌면서
    for i in range(len(s)):
        # 만약 문자열의 i번째가 '('라면
        if s[i] == '(':
            # 덱에 삽입
            stack.append(s[i])
        # 만약 문자열의 i번째가 ')'일 경우
        elif s[i] == ')':
            # d가 비어있다면 False
            if not stack:
                return False
            # 비어있지 않다면
            else:
                stack.pop()
    # d에 남아있는 요소가 존재한다면 False
    if stack:
        return False
    return True


s = "()()"
print(solution(s))
s = ")()("
print(solution(s))
