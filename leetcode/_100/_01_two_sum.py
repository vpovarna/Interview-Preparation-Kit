from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    dic = dict()
    for i, n in enumerate(nums):
        new_target = target - n
        if new_target in dic:
            return [dic[new_target], i]
        dic[n] = i
