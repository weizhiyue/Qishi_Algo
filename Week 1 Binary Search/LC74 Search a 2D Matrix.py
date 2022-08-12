#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 23:36:44 2022

@author: zhiyuewei
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ### Convert the matrix into a one dimensional array
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left + 1 < right:
            mid = (left + right) // 2
            row, col = mid // n, mid % n
            if matrix[row][col] > target:
                right = mid
            elif matrix[row][col] < target:
                left = mid
            else:
                return True
        
        row_left, col_left = left // n, left % n
        row_right, col_right = right // n, right % n
        if matrix[row_left][col_left] == target:
            return True
        elif matrix[row_right][col_right] == target:
            return True
        return False
    

if __name__ == '__main__':
    sol = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    print(sol.searchMatrix(matrix, 3))
    print(sol.searchMatrix(matrix, 13))