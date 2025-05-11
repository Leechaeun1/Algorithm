import itertools
import math

def solution(nums):
    # nums에서 3개를 뽑고, 3개씩 더하는 경우의 수
    caselist = list(itertools.combinations(nums, 3))
    sumlist = [sum(i) for i in caselist]
    sumlist.sort()

    # 소수 갯수 구하기
    result = 0
    for i in sumlist:
        if i == 1:
            continue
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            result += 1
    return result


nums = [1, 2, 3, 4]
print(solution(nums))
nums = [1, 2, 7, 6, 4]
print(solution(nums))
