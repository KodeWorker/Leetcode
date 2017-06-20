class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    # island
                    n = 4
                    if i > 0 and grid[i-1][j]:
                        n -= 1
                    if i < len(grid) - 1 and grid[i+1][j]:
                        n -= 1
                    if j > 0 and grid[i][j-1]:
                        n -= 1
                    if j < len(grid[i]) - 1 and grid[i][j+1]:
                        n-= 1
                    total += n
#                else:
#                    # ocean
#                    pass
                
        return total

if __name__ == '__main__':
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    sol = Solution()
    n = sol.islandPerimeter(grid)
    print(n)