# little bit slow: 772 ms (37.85%)
# the FAST 1-line version: return int((math.sqrt(8*n + 1) - 1)/2)

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        size = 0
        if n == 1:
            return 1
        else:
            while n > 0:
                size += 1
                n -= size 
            if n == 0:
                return size
            else:
                return max(0, size - 1)
    
if __name__ == '__main__':
    n = 0
    row = Solution().arrangeCoins(n)
    print(row)