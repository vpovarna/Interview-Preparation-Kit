from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        for i, n in enumerate(nums):
            new_target = target - n
            if new_target in dic:
                return [dic[new_target], i]
            else:
                dic[n] = i