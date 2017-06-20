class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        return -1 if a==b else max(len(a),len(b))

if __name__ == '__main__':
#    a = "aba"
#    b = "cdc"
    
    a = "aaa"
    b = "ccc"
    sol = Solution()
    o = sol.findLUSlength(a, b)
    print(o)