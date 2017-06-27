import math

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # definition of trailing-zero problem in wikipedia
        # https://en.wikipedia.org/wiki/Trailing_zero
        if n > 0:
            k = int(math.floor(math.log(n, 5)))
        else:
            k = 0
        trailing_zeroes = 0
        for i in range(1, k+1):
            trailing_zeroes += int(math.floor(n/(5**i)))
        return trailing_zeroes   

if __name__ == '__main__':
    n = 0
    print(Solution().trailingZeroes(n))