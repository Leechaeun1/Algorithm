class Solution(object):
    def twoSum(self, nums, target):
        # 튜플로 변환해서 정렬
        nums_with_index = [(num, i) for i, num in enumerate(nums)]
        nums_with_index.sort(key=lambda x: x[0])  # 숫자 기준으로 정렬
        # 시작, 끝 인덱스 번호 지정
        start, end = 0, len(nums) - 1
        # start가 end 보다 작을때
        # start, end 튜플의 0번째 요소끼리 더한다
        while start < end:
            Sum = nums_with_index[start][0] + nums_with_index[end][0]
            # 합이 target보다 클 경우 end--
            if Sum > target:
                end -= 1
            # 합이 target보다 작을 경우 start++
            elif Sum < target:
                start += 1
            # start, end의 1번째 요소 리턴
            else:
                return [nums_with_index[start][1], nums_with_index[end][1]]


nums = [3, 2, 4]
target = 6
solution = Solution()
print(solution.twoSum(nums, target))