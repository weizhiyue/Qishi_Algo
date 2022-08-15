#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 14:37:39 2022

@author: zhiyuewei
"""

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        ### Guess and check using binary search
        # n integers and X, minimum number of subarrays needs to be divided into such that no subarray sum is greater than X
        low, high = max(nums), sum(nums)
        
        ### Logic in the binary search
        while low + 1 < high:
            mid = (low + high) // 2
            # Find the number of divide num corresponding to mid
            num_split = self.find_divide_num(nums, mid)
            if num_split <= m:
                # If the minimum # of subarray needed to be divided is less or equal to m, then we can try a smaller X (# of subarray will increase)
                high = mid
            else:
                # If we need subarrays more than m to get X, then we need to search for a larger X (# of subarray will decrease)
                low = mid
        
        # Last case in the loop: low + 1 = mid, mid + 1 = high
        # Exit the loop: low + 1 == high
        # Either low or high has not been inspected
        low_split = self.find_divide_num(nums, low)
        high_split = self.find_divide_num(nums, high)
        if low_split <= m:
            return low
        if high_split <= m:
            return high

    
    def find_divide_num(self, nums, x):
        """
        Find the minimum number of subarrays needs to be divided into s.t. no subarray sum is greater than X
        x: the guessed largest subarray sum
        """
        splitsRequired = 0
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum > x:
                # Start a new split
                curr_sum = nums[i]
                splitsRequired += 1
        return (splitsRequired + 1)


if __name__ == '__main__':
    sol = Solution()
    nums = [7,2,5,10, 8]
    print(sol.splitArray(nums, 2))