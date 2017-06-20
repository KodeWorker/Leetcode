class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) != 0:
            for i in range(1,len(strs)):
                strs[i] = self.getCommonPrefix(strs[i-1], strs[i])
            return strs[-1]
        else:
            return ""
        
    def getCommonPrefix(self, string1, string2):
        common_length = min(len(string1), len(string2))
        ind = 0
        while ind < common_length:
            if string1[ind] == string2[ind]:
                ind += 1
            else:
                break
        return string1[:ind]
        

if __name__ == '__main__':
    strs = []
    sol = Solution()
    o = sol.longestCommonPrefix(strs)
    print(o)