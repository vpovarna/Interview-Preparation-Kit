class Solution:
    def makeGood(self, s: str) -> str:
        
        def remove_chars(s: str) -> int:
            for i in range(len(s) - 1):
                if s[i] != s[i+1] and (s[i] == s[i+1].upper() or s[i].upper() == s[i+1]):
                   return i
            return -1

        index = remove_chars(s)
        while index != -1:
            s = s[:index] + s[(index +2):]        
            index = remove_chars(s)
        return s

if __name__ == "__main__":
    print(Solution().makeGood("leEeetcode"))
    print(Solution().makeGood("abBAcC"))
    print(Solution().makeGood("kkdsFuqUfSDKK"))