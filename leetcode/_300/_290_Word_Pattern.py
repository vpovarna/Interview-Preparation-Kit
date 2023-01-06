class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        dic = {}

        if len(pattern) != len(words):
            return False
        if len(set(pattern)) != len(set(words)):
            return False

        for i in range(len(words)):
            if words[i] not in dic:
                dic[words[i]] = pattern[i]
            elif dic[words[i]] != pattern[i]:
                return False
        return True


def main():
    solution = Solution()
    print(solution.wordPattern("abba", "dog cat cat dog"))  # false
    print(solution.wordPattern("abba", "dog cat cat fish"))  # false


if __name__ == '__main__':
    main()
