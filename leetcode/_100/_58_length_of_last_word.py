class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = [w for w in s.split(" ") if w !=""]
        return len(words[-1])

if __name__ == "__main__":
    print(Solution().lengthOfLastWord("   fly me   to   the moon  "))
