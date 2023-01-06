from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = dict()

        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in dic:
                dic[sorted_s].append(s)
            else:
                dic[sorted_s] = [s]

        return list(dic.values())


if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
