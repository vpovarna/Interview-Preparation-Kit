from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        remaining_coins = coins

        for c in costs:
            if c > remaining_coins:
                return count
            remaining_coins -= c
            count += 1
        return count


if __name__ == '__main__':
    print(Solution().maxIceCream([1, 3, 2, 4, 1], 7))
    print(Solution().maxIceCream([10, 6, 8, 7, 7, 8], 5))
