from typing import List


#121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_value = float("inf")

        for price in prices:
            if price < min_value:
                min_value = price
            elif price - min_value > max_profit:
                max_profit = price - min_value
            else:
                continue
        return max_profit


if __name__ == '__main__':
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
