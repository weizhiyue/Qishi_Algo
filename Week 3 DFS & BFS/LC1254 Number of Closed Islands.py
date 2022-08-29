class Solution(object):
    def closedIsland(self, grid):
        """
        Counts closed islands in the given grid
        :param grid: Grid representing area
        :return: Count of closed islands
        """
        ### Find the connected components (only "0"s) that are not on the edges
        count = 0
        self.grid = grid
        
        ### Utilize DFS to find the closed island
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.grid[i][j] == 0 and self.checkconnected_dfs(self.grid, i, j):
                    count += 1
        return count
    
    def checkconnected_dfs(self, grid, i, j):
        ### Check if the current cell exceeds the coundary
        # If one connected component is on the edge, it will return False
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return False
        
        
        if grid[i][j] == 1:
            return True
        
        # Mark the cell as visited
        grid[i][j] = 1
        
        # Check four directions
        res = True
        res &= self.checkconnected_dfs(grid, i-1, j) # up
        res &= self.checkconnected_dfs(grid, i+1, j) # down
        res &= self.checkconnected_dfs(grid, i, j-1) # left
        res &= self.checkconnected_dfs(grid, i, j+1) # right
        
        return res
        
