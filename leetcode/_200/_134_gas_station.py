from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        gas = gas + gas
        cost = cost + cost

        start, current = 0, 0

        for i, (c, g) in enumerate(zip(cost, gas)):
            current += g
            current -= c

            if current < 0:
                start = i + 1
                current = 0
            else:
                if i - start >= N:
                    return start

        return -1


if __name__ == '__main__':
    print(Solution().canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
