# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

# ---> Example
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Input: nums = [1,3,5,6], target = 7
# Output: 4

# TC = 0(log n)


class Solution:
    def searchInsert(self, nums, target):
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2
            mid_value = nums[mid]

            if mid_value == target:
                return mid

            if target > mid_value:
                start = mid + 1
            else:
                end = mid - 1
        return start
