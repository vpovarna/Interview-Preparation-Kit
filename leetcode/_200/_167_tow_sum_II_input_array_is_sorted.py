from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer = 0
        right_pointer = len(numbers) - 1

        while left_pointer < right_pointer:
            if numbers[left_pointer] + numbers[right_pointer] == target:
                return [left_pointer + 1, right_pointer + 1]
            elif numbers[left_pointer] + numbers[right_pointer] > target:
                right_pointer -= 1
            else:
                left_pointer += 1


if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))
    print(Solution().twoSum([2, 3, 4], 6))
