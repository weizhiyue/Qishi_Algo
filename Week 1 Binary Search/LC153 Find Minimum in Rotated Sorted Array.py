#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 11:05:44 2022

@author: zhiyuewei
"""

### Solution 1
class Solution1(object):
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
                
        # Using "<=" here in case there is only one element in the array
        if nums[start] <= nums[end]:
            return nums[start]
        elif nums[start] > nums[end]:
            return nums[end]
        

### Solution 2: Using inflection point
class Solution2(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ### nums: unique elements
        ### Another idea: find the index of the inflection point
        start, end = 0, len(nums) - 1
        
        # If the array is not a rotated array
        if nums[start] <= nums[end]:
            return nums[start]
        
        # If the array is rotated
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] >= nums[start]:
                # The inflection point is on the RHS of mid
                start = mid
            else:
                # The inflection point is on the LHS of mid
                end = mid
        
        # Exiting the loop: start + 1 == end
        if nums[start] > nums[end]:
            return nums[end]
        else:
            return nums[start]        
        
if __name__ == '__main__':
    sol = Solution()
    print(sol.findMin([3, 4, 5, 1, 2]))
    print(sol.findMin([4, 5, 6, 7, 0, 1, 2]))
    print(sol.findMin([11, 13, 15, 17]))
          
