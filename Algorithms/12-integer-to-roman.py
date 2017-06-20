class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
#        R = ['M': 1000,
#             'CM': 900,
#             'D': 500,
#             'CD': 400,
#             'C': 100,
#             'XC': 90,
#             'L': 50,
#             'XL':40,
#             'X': 10,
#             'IX': 9,
#             'V': 5,
#             'IV': 4,
#             'I': 1]

        N = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        C = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        out = ''
        m = num
        
#        for key in R.keys():
#            out += m // R[key] * key
#            m %= R[key]        
        for i in range(len(N)):
            out += m // N[i] * C[i]
            m %= N[i]
            
        return out
    
if __name__ == '__main__':
    num = 4
    sol = Solution()
    o = sol.intToRoman(num)
    print(o)