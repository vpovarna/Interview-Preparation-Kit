from typing import List


def twoNumberSum(array: List[int], target: int) -> List[int]:
    numbers = set()
    for n in array:
        new_target_sum = target - n
        if new_target_sum in numbers:
            return [n, new_target_sum]
        else:
            numbers.add(n)

    return []


# two passes
def twoNumberSum2(array: List[int], target: int) -> List[int]:
    numbers = set(array)
    for n in array:
        new_target = target - n
        if new_target in numbers and n is not new_target:
            return [n, new_target]

    return []


if __name__ == '__main__':
    print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))  # [-1, 11]
    print(twoNumberSum2([3, 5, -4, 8, 11, 1, -1, 6], 10))  # [-1. 11]
    print(twoNumberSum([15], 15))  # []
    print(twoNumberSum([14], 15))  # []
