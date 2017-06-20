# too slow
# this is roughly O(n*n)
#class Solution(object):
#    def singleNumber(self, nums):
#        """
#        :type nums: List[int]
#        :rtype: int
#        """
#        ind = 0
#        while ind < len(nums):
#            num = nums[0]
#            nums = nums[1:]
#            try:
#                nums.remove(num)
#                ind -= 1
#            except:
#                break
#            ind += 1
#        return num


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        out = 0
        for i in nums:
            out ^= i            
        return out

if __name__ == '__main__':
#    nums = [1] # 1
#    nums = []
#    nums = [2,2,3,3,7,7,4] # 4
    nums = [2,3,1,2,1]
    sol = Solution()
    num = sol.singleNumber(nums)
    print(num)