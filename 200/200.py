class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def set_zero(grid, i, j):
            if grid[i][j] == '0':
                return
            else:
                grid[i][j] = '0'
                if i + 1 < len(grid):
                    set_zero(grid, i + 1, j)
                if j + 1 < len(grid[0]):
                    set_zero(grid, i, j+1)
                if i - 1 >= 0:
                    set_zero(grid, i - 1, j)
                if j - 1 >= 0:
                    set_zero(grid, i, j - 1)

        num = 0
        if grid == [] or grid == [[]]:
            return 0
        else:
            for row in range(len(grid)):
                for column in range(len(grid[0])):
                    if grid[row][column] == '1':
                        num = num + 1
                        set_zero(grid, row, column)

        return num

grid = [["1","1","1"],["0","1","0"],["1","1","1"]]
Solution().numIslands(grid)