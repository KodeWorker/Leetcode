class Solution(object):    
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        # remember to read the question carefully and be a lil bit creative!
        # cuz, the instruction is totaly scheit!
        
        output = []
        for element in findNums:
            
            ind = nums.index(element)
            rest = nums[ind:]
#            print(element, rest)
#            print(rest)
            
            if len(rest) == 0:
                output.append(-1)
            else:
                ind_ = 0
                while ind_ < len(rest):
#                    print(element, rest, ind_)
                    if ind_ + 1 < len(rest) and rest[ind_ + 1] > element:
                        output.append(rest[ind_+1])
                        break
                    else:
                        ind_ += 1
                if ind_ == len(rest):
                    output.append(-1)
        return output

if __name__ == '__main__':
    n1 = [2,4] ; n2 = [1,2,3,4]
    
#    [-1,3,-1]
#    n1 = [4,1,2]
#    n2 = [1,3,4,2]

#    [3,-1]   
#    n1 = [2,4]
#    n2 = [1,2,3,4]

#    [-1,3,-1]
#    n1 = [4,1,2]
#    n2 = [1,3,4,2]

#    [3, 1, 1]
#    n1 = [2,1,3]
#    n2 = [2,3,1]
    sol = Solution()
    o = sol.nextGreaterElement(n1, n2)
    print(o)