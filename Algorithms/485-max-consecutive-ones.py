class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLen = 0
        
        ind = 0
        count = 0
        while ind < len(nums):
            
            if nums[ind]:
                count += 1
            else:
                if count > maxLen:
                    maxLen = count
                count = 0
            ind += 1
        if count > maxLen:
            maxLen = count    
        return maxLen

if __name__ == '__main__':
    nums = [1,1,0,1,1,1] # 3
    sol = Solution()
    n = sol.findMaxConsecutiveOnes(nums)
    print(n)