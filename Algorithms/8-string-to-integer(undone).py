# unclear question 

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        n_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        op_set = {'+', '-'}
        
        init = None
        end = None
        for i in range(len(str)):
            if str[i] in n_set | op_set and init == None:
                init = i
            elif str[i] not in n_set and init != None:
                end = i
                break
        
        if init == None:
            return 0
        elif len(str[init:end].replace('+', '')) == 0:
            return 0
        else:
            
            out = str[init:end].replace('-', '-0')
            out = int(out.replace('+', '+0'))
            return out
            
        
if __name__ == '__main__':
#    s = 'cxcsafdf33df'
#    s = '123+12'
#    s = '23sddd+123'
#    s = 'dfew'
#    s = '                010'
#    s = '+'
#    s = '-'
#    s = "     +004500"
#    s = "   +0 123"

    s = "2147483648" # -> 2147483647 ?
    sol = Solution()
    o = sol.myAtoi(s)
    print(o)    
