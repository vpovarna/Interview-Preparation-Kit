from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start_pointer, end_pointer = 0, len(height) - 1
        result = 0
        while start_pointer < end_pointer:
            if height[start_pointer] < height[end_pointer]:
                tmp_result = height[start_pointer] * (end_pointer - start_pointer)
                result = max(result, tmp_result)
                start_pointer += 1
            else:
                tmp_result = height[end_pointer] * (end_pointer - start_pointer)
                result = max(result, tmp_result)
                end_pointer -= 1
        return result


if __name__ == '__main__':
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
