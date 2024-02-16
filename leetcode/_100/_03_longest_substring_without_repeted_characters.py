class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        p = 0
        res = 0
        
        for i, c in enumerate(s):
            while c in visited:
                visited.remove(s[p])
                p += 1
            visited.add(s[i])
            res = max(res, i -p + 1)
        return res


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("bbbbb"))
    print(Solution().lengthOfLongestSubstring("pwwkew"))
