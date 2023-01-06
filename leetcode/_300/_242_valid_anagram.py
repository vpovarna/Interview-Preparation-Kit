class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def word_letter_occurrence(word: str) -> dict[str, int]:
            dic = dict()
            for c in word:
                dic[c] = dic.get(c, 0) + 1
            return dic

        return word_letter_occurrence(s) == word_letter_occurrence(t)

    # Optimal solution
    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s, count_t = dict(), dict()
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        return count_s == count_t


if __name__ == '__main__':
    print(Solution().isAnagram2("anagram", "nagaram"))
