class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        ro = len(nums)
        co = len(nums[0])
        out = []
        if co*ro == r*c:
            flatten = [item for row in nums for item in row]
            for i in range(0, len(flatten), c):
                out.append(flatten[i:i+c]) 
            return out
        else:
            return nums

if __name__ == '__main__':
    m = [[1,2],[3,4]]
    r=2
    c=2
    sol = Solution()
    o = sol.matrixReshape(m,r,c)
    print(o)