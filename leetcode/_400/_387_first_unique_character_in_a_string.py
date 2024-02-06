from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = defaultdict(int)

        for c in s:
            dict[c] +=1

        for index, char in enumerate(s):
            if dict[char] == 1:
                return index

        return -1

if __name__ == '__main__':
    print(Solution().firstUniqChar("leetcode"))
    print(Solution().firstUniqChar("loveleetcode"))
