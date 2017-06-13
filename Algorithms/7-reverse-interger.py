class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        r =  int(str(abs(x))[::-1]) * (1, -1)[x < 0]
        # check if overflow 
        # 32-bit signed integer
        
        if x > 0:
            bits = len(str(bin(r))) - 2
        else:
            bits = len(str(bin(r))) - 3
#        print(bits, bin(r))
        # one bit for sign !!!!!!!
        if bits <= 31:
            return r
        else:
            return 0

if __name__ == '__main__':
#    x = -123
#    x = 1534236469
    x = 1563847412
#    x = 2147483647
    sol = Solution()
    o = sol.reverse(x)
    print(o)