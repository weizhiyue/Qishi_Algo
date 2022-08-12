class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ### Binary Search
        # (n + 1) elements in [1, n]
        # Take the number from 1 to n and count how many number that are less than or equal to the selected number
        n = len(nums) - 1
        start, end = 1, n
        
        res = end
        while start + 1 < end:
            mid = (start + end) // 2
            print(start, end, mid)
            # Count how many numbers are less or equal to mid
            count = sum(num <= mid for num in nums)
            if count > mid:
                # The duplicate number can be on the LHS of mid
                res = mid
                end = mid
            else:
                # The duplicate number is on the RHS of mid
                start = mid
        
        count_l = sum(num <= start for num in nums)
        count_r = sum(num <= end for num in nums)
        if count_l > start:
            res = start
        else:
            res = end
        
        return res
