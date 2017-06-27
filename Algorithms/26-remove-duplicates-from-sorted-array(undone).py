class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # desription dosen't fit the test case!
        if len(nums) == 0:
            return 0
        else:
            out = []
            while len(nums) > 0:
                s = nums[0]
                out.append(s)
                while s in nums:
                    nums.remove(nums[0])
            return out
    
if __name__ == '__main__':
    nums = [1]
    print(Solution().removeDuplicates(nums))