from collections import defaultdict


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ans = [0] * len(s)

        nr_of_one = 0
        for c in s:
            if c == "1":
                nr_of_one += 1
                
        for i in range(nr_of_one - 1):
            ans[i] = 1
        
        ans[-1] = 1
        
        return "".join(str(i) for i in ans)

if __name__ == "__main__":
    print(Solution().maximumOddBinaryNumber("0101"))