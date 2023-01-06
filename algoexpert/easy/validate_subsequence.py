from typing import List


# solution 1
def isValidSubsequence(array: List[int], sequence: List[int]) -> bool:
    i, j = 0, 0

    while i < len(array):
        if array[i] == sequence[j]:
            j += 1
        if j == len(sequence):
            return True
        i += 1

    return False


# solution 2
def isValidSubsequence2(array: List[int], sequence: List[int]) -> bool:
    j = 0

    for i in range(len(array)):
        if array[i] == sequence[j]:
            j += 1
        if j == len(sequence):
            return True

    return False
