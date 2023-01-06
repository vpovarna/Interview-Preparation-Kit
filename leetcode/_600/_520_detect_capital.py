class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return len(word) <= 1 or word[1:].islower() or word.isupper()


if __name__ == '__main__':
    print(Solution().detectCapitalUse("USA"))
    print(Solution().detectCapitalUse("FlaG"))
    print(Solution().detectCapitalUse("leetcode"))
    print(Solution().detectCapitalUse("Google"))
