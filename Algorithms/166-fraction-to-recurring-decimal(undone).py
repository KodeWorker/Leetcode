class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        int_string = ""
        dec_string = ""
        while numerator != 0:
            #string += str(numerator//denominator)
            numerator %= denominator
            if numerator != 0:
                if len(int_string) == 0:
                    int_string = str(numerator//denominator)
                elif len(dec_string)>2 and dec_string[-1] != "0" and dec_string[-1] == dec_string[-2]:
                    dec_string = "%s(%s)" %(dec_string[:-2], dec_string[-2])
                    break
                elif len(dec_string)>0 and len(dec_string) %2 == 0 and dec_string[:int(len(dec_string)/2)] == dec_string[int(len(dec_string)/2):]:
                    dec_string = "(%s)" %dec_string[:int(len(dec_string)/2)]
                    break
                #else:
                dec_string += str(numerator*10 // denominator)
                numerator *= 10
                
        if len(dec_string) != 0:
            string = "%s.%s" %(int_string, dec_string)
        else:
            string = "%s" % int_string
        return string

if __name__ == '__main__':
#    numerator = 1
#    denominator = 333

    numerator = 1
    denominator = 6
    
#    numerator = 1
#    denominator = 99
    string = Solution().fractionToDecimal(numerator, denominator)
    print(string)