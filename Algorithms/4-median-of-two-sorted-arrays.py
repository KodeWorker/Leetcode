class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = sorted(nums1+nums2)
        if len(total)!=0 and len(total) % 2 == 0:
            return (total[int(len(total)/2)] + total[int(len(total)/2) - 1])/float(2)
        elif len(total)!=0:
            return total[int(len(total)/2)]
        else:
            return 0

if __name__ == '__main__':
    
    nums1 = [1,2]
    nums2 = [3,4]
    
    sol = Solution()
    s = sol.findMedianSortedArrays(nums1, nums2)
    print(s)