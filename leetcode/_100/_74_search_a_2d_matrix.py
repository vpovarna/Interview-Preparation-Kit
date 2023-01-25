from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in range(len(matrix)):
            if target in matrix[i]:
                return target in matrix[i]

    def searchMatrixBS(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix[0]), len(matrix)
        beg, end = 0, m * n - 1

        while beg < end:
            mid = beg + ((end - beg) // 2)
            print("mid: ", mid)
            print(matrix[mid // m][mid%m])

            if matrix[mid // m][mid%m] < target:
                beg = mid + 1
            else:
                end =  mid 
        return matrix[beg//m][beg%m] == target



if __name__ == '__main__':
    print(Solution().searchMatrixBS(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))