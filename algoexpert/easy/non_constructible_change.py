from typing import List


def nonConstructibleChange(coins: List[int]) -> int:
    coins.sort()
    res = 0
    for coin in coins:
        if coin > res + 1:
            return res + 1
        else:
            res += coin
    return res + 1


if __name__ == '__main__':
    print(nonConstructibleChange([5, 7, 1, 1, 2, 3, 22]))
