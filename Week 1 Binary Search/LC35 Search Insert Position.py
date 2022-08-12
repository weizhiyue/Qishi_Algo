#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 23:31:38 2022

@author: zhiyuewei
"""

#### Template 1
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        left, right = 0, len(nums) - 1
        ### Search [left, right]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        
        ### When the loop terminates, we have: right < left
        ### Where nums[right] < target < nums[left]
        return left
    

if __name__ == '__main__':
    sol = Solution()
    nums= [1, 3, 5, 6]
    print(sol.searchInsert(nums, -1))
    print(sol.searchInsert(nums, 7))
    print(sol.searchInsert(nums, 4))