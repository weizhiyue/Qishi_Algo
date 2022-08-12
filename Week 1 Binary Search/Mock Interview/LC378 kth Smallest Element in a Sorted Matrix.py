class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        ### Rows and columns are in ascending order
        ### Another form of the binary search
        n = len(matrix)
        start, end = matrix[0][0], matrix[n - 1][n - 1]

        while start < end:
            mid = (start + end) / 2
            smaller, larger = matrix[0][0], matrix[n - 1][n - 1]
            count, smaller, larger = self.CountLessEqual(matrix, mid, smaller, larger)
            
            ### Compare if there is enough elements for k
            if count == k:
                return smaller
            elif count < k:
                # If k is more than count, search in [larger, end]
                start = larger
            else:
                # If k is less than count, search in [start, smaller]
                end = smaller
        # When we jump out of the loop, we have: start == end
        return start
    
    
    def CountLessEqual(self, matrix, mid, smaller, larger):
        """
        smaller: the largest element smaller than mid
        larger: the smallest element larger than mid
        """
        # Start from the bottom-left cornor of the matrix
        n = len(matrix)
        row, col = n - 1, 0
        count = 0
        
        while row >= 0 and col <= (n - 1):
            if matrix[row][col] > mid:
                # update the larger and move up for one row
                larger = min(larger, matrix[row][col])
                row -= 1
            elif matrix[row][col] <= mid:
                # Update the smaller and move right for one column
                smaller = max(smaller, matrix[row][col])
                col += 1
                count += (row + 1) 
        return count, smaller, larger
        

# Question: can we use template 2?
