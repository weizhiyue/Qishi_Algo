class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        # Initate BFS from all gates at the same time
        # Enqueue the gates at the same time
        m = len(rooms)
        if m == 0:
            return
        n = len(rooms[0])
        queue = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        
        # All the possible directions
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while len(queue) != 0:
            top_cell = queue.pop(0)
            row, col = top_cell[0], top_cell[1]
            for dirct in directions:
                new_row, new_col = row + dirct[0], col + dirct[1]
                if new_row < 0 or new_row >= m or new_col < 0 or new_col >= n or rooms[new_row][new_col] != (2 ** 31 - 1):
                    continue
                rooms[new_row][new_col] = rooms[row][col] + 1
                queue.append((new_row, new_col))
    
        ### It's smart to enqueue all the 0s at the same time, rather than empty the queue of one 0 and enqueue the next. 
        ### So whenever an empty room is reached, it must be from the closest gate.
        
        ### Time complexity: O(mn), each rooms is visited at most once
        ### Space complexity: O(mn), the size of the queue
