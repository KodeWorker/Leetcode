class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # wining condition: you take turns and it remains 4 stones in the heap
        if n % 4 == 0:
            return False
        else:
            return True

if __name__ == '__main__':
    n = 1
    sol = Solution()
    o = sol.canWinNim(n)
    print(o)