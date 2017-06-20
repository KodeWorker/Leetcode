import time


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        pattern_len = (2 * numRows - 2)
        
        if pattern_len != 0:
            
            repeated = (len(s) - 1) // pattern_len
            remainder = (len(s) - 1) % pattern_len
            
#            print(pattern_len,repeated,remainder)
            
            s += ' ' * (pattern_len - remainder)
            out = s[0]
            for i in range(repeated+1):
                out += (s[i*pattern_len + pattern_len])
            for j in range(1,numRows-1):
                for i in range(repeated+1):                
                    out+= s[i*pattern_len + j] + s[i*pattern_len + pattern_len - j]
            for i in range(repeated+1):
                out+= s[i*pattern_len + numRows - 1]
            return out.replace(' ', '')
#            return out
         
        else:
            return s
        
        
if __name__ == '__main__':
    t0 = time.time()
    s = ''
#    s = 'A'
#    s = 'PAYP'
#    s = "PAYPALISHIRING"
#    numRows = 1
    s = "PAYPALISHIRING"
    numRows = 4
    # "PAHNAPLSIIGYIR"
    
    sol = Solution()
    o = sol.convert(s, numRows)
    
    print(o)
    
    print(time.time()-t0)    