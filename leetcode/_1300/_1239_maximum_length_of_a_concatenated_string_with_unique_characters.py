from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:

        def is_unique(s):
            return len(s) == len(set(s))

        def backtracking(index, current, max_length):
            max_length[0] = max(max_length[0], len(current))

            for i in range(index, len(arr)):
                if is_unique(current + arr[i]):
                    backtracking(i + 1, current + arr[i], max_length)

        max_length = [0]
        backtracking(0, "", max_length)
        return max_length[0]


if __name__ == '__main__':
    print(Solution().maxLength(["un", "iq", "ue"]))
