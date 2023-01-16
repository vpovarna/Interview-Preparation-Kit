class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {')': '(', ']': '[', '}': "{"}

        stack = []
        for c in s:
            if c not in parentheses:
                stack.append(c)
                continue

            if len(stack) == 0 or stack[-1] != parentheses[c]:
                return False
            else:
                stack.pop()

        return len(stack) == 0


if __name__ == '__main__':
    print(Solution().isValid("()[]{}"))
    print(Solution().isValid("(]"))
    print(Solution().isValid("()"))
