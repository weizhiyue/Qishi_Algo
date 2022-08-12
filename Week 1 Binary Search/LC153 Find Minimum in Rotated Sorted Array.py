#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 11:05:44 2022

@author: zhiyuewei
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Find the original array?
        # Assume the nums array is not empty
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                # When end < start <= mid, the minimum is on the RHS of mid
                start = mid
            else:
                # When mid <= end, there are two scenarios:
                # 1. start <= mid <= end (minimum is start)
                # 2. mid <= end < start (minimum is between start and end)
                # For both of these scenarios, the minimum is always on the LHS of mid
                end = mid
                
        
        if nums[start] <= nums[end]:
            return nums[start]
        elif nums[start] > nums[end]:
            return nums[end]
        
        
if __name__ == '__main__':
    sol = Solution()
    print(sol.findMin([3, 4, 5, 1, 2]))
    print(sol.findMin([4, 5, 6, 7, 0, 1, 2]))
    print(sol.findMin([11, 13, 15, 17]))
          