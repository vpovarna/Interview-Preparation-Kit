from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+", "-", "*", "/"}

        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(b - b)
                if token == "*":
                    stack.append(a * b)
                if token == "/":
                    stack.append(int(b / a))

        return stack[0]


if __name__ == '__main__':
    print(Solution().evalRPN(["2", "1", "+", "3", "*"]))
    print(Solution().evalRPN(["4", "13", "5", "/", "+"]))
    print(Solution().evalRPN(["10", "6", "9", "3",
          "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
