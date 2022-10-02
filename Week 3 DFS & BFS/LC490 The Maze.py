class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        ### Create a visited 2D array
        ### Check every possible path from the curr starting pt
        visited = [[False for i in range(len(maze[0]))] for j in range(len(maze))]
        return self.dfs(maze, start, destination, visited)
    
    def dfs(self, maze, start, destination, visited):
        # Check if the starting pt has been marked
        row, col = start[0], start[1]
        if visited[row][col]:
            return False
        # Check if the destination has been reached
        if row == destination[0] and col == destination[1]:
            return True
        # Mark the current starting pt
        visited[row][col] = True
        
        # Traverse all four directions
        # Right: roll to the right until hit the wall
        r = col + 1
        while r < len(maze[0]) and maze[row][r] == 0:
            r += 1
        if self.dfs(maze, [row, r - 1], destination, visited):
            return True
        # Left: roll to the left until hit the wall
        l = col - 1
        while l >= 0 and maze[row][l] == 0:
            l -= 1
        if self.dfs(maze, [row, l + 1], destination, visited):
            return True
        # Up
        up = row - 1
        while up >= 0 and maze[up][col] == 0:
            up -= 1
        if self.dfs(maze, [up + 1, col], destination, visited):
            return True
        # Down
        down = row + 1
        while down < len(maze) and maze[down][col] == 0:
            down += 1
        if self.dfs(maze, [down - 1, col], destination, visited):
            return True
