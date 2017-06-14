class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
#        N = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
#        C = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        
        C1 = ['CM','CD','XC','XL','IX','IV']
        C2 = ['M','D','C','L','X','V','I']
        N1 = [900,400,90,40,9,4]
        N2 = [1000,500,100,50,10,5,1]
        
        string = s
        out = 0
        
        for i in range(len(C1)):
            try:
                ind = string.index(C1[i])
                out += N1[i]
                string = string[:ind] + string[ind+len(C1[i]):]
            except:
                pass
        
        while len(string) != 0:
            for i in range(len(C2)):
                try:
                    ind = string.index(C2[i])
                    out += N2[i]
                    string = string[:ind] + string[ind+1:]
                except:
                    pass
        return out
    
if __name__ == '__main__':
    s= 'MCMXCVI' # 1996
    sol = Solution()
    o = sol.romanToInt(s)
    print(o)