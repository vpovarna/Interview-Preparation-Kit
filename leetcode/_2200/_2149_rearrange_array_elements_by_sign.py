from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_numbers = [x for x in nums if x >= 0]
        negative_numbers = [x for x in nums if x < 0]

        assert (len(positive_numbers) == len(negative_numbers))

        for i in range(0, len(positive_numbers)):
            nums[2*i] = positive_numbers[i]
            nums[2*i + 1] = negative_numbers[i]

        return nums


if __name__ == '__main__':
    print(Solution().rearrangeArray([3, 1, -2, -5, 2, -4]))
