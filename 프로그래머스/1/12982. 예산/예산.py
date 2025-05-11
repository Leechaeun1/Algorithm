def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        if i <= budget:
            budget -= i
            answer += 1
    return answer

d = [1, 3, 2, 5, 4]
budget = 9
print(solution(d, budget))

d = [2, 2, 3, 3]
budget = 10
print(solution(d, budget))