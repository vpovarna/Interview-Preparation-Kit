from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        count = 0

        for i in range(n):
            arr = []
            for str in strs:
                arr.append(str[i])

            if arr != sorted(arr):
                count += 1

        return count

    def minDeletionSize2(self, strs: List[str]) -> int:
        counter = 0
        for i in zip(*strs):
            if list(i) != sorted(list(i)):
                counter += 1

        return counter


if __name__ == '__main__':
    print(Solution().minDeletionSize2(["abc", "bce", "cae"]))
