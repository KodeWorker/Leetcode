class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        
        init, end = 0, len(s) - 1
        while end > init:
            if s[init] == s[end]:
                init += 1
                end -= 1
            else:
                return False
        return True
            
        
if __name__ == '__main__':
    x = 12321
    sol = Solution()
    o = sol.isPalindrome(x)
    print(o)  