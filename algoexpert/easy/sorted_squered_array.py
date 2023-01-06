import math
from typing import List


def sortedSquaredArray(array: List[int]) -> List[int]:
    sqrt_array = [int(math.pow(x, 2)) for x in array]
    return sorted(sqrt_array)


if __name__ == '__main__':
    print(sortedSquaredArray([1, 2, 3, 5, 6, 8, 9]))
    print(sortedSquaredArray([-2, -1]))
    print(sortedSquaredArray([-10, -5, 0, 5, 10]))
