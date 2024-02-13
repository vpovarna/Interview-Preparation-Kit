from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.isPalindrome(word):
                return word
        return ""

    def isPalindrome(self, input: str) -> bool:
        l, r = 0, len(input) - 1

        while l <= r:
            if input[l] != input[r]:
                return False
            l += 1
            r -= 1
        return True


if __name__ == '__main__':
    print(Solution().firstPalindrome(["abc", "car", "ada", "racecar", "cool"]))
