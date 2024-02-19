class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        
        while n % 2 == 0:
            n = n / 2
        return n == 1

if __name__ == '__main__':
    print(Solution().isPowerOfTwo(16))
