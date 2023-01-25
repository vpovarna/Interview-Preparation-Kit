from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []

        for current_index, temperature in enumerate(temperatures):
            while len(stack) > 0 and temperature > stack[-1][0]:
                _, last_index = stack.pop()
                output[last_index] = current_index - last_index
            
            stack.append((temperature, current_index))


        return output

if __name__ == '__main__':
    print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))
        