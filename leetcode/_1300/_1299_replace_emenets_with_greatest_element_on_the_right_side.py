from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr.append(-1)
        for i in range(len(arr) - 2, -1, -1):
            arr[i] = max(arr[i], arr[i+1])
        return arr[1:]

    
if __name__ == "__main__":    
    print(Solution().replaceElements([17,18,5,4,6,1]))
    print(Solution().replaceElements([400]))