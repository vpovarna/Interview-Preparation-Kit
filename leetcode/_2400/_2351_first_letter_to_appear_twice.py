from collections import defaultdict

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        visited = set()
        
        for c in s:
            if c in visited:
                return c
            else:
                visited.add(c)

if __name__ == '__main__':
    print(Solution().repeatedCharacter("abcdd"))
    print(Solution().repeatedCharacter("abccbaacz"))
