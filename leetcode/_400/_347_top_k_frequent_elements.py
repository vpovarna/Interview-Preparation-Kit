from typing import List, Dict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            dic[num] = 1 + dic.get(num, 0)

        for n, c in dic.items():
            freq[c].append(n)

        res = []
        # freq is updated in the number of occurrence. This is why the traversal is done from the end
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


if __name__ == '__main__':
    print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
    print(Solution().topKFrequent([4, 1, -1, 2, -1, 2, 3], 2))
