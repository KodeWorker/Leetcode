class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        bro = []
        s = sorted(candies)
        ind = 0
        while ind < len(s):
            if ind > 0 and s[ind] == s[ind-1]:
                ind += 1
                continue
            else:
                
                bro.append(s[ind])
            ind += 1
        return min(len(bro), int(len(candies)/2) ) 
        # remember bro cannot take more than half!
        # take care your lil sis , do as your father said! 
            
if __name__ == '__main__':
    s = [1,1,2,3]
#    s = [0,0,14,0,10,0,0,0]
#    s = [0,0,0,0,0,0,0,3,5,7]
    sol = Solution()
    o = sol.distributeCandies(s)
    print(o)