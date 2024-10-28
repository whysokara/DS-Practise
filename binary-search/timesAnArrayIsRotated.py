
# arr = [6,7,8,1,2,3,4,5]
# def some(arr):
#   for i in range(len(arr)-1):
#     if arr[i+1] < arr[i]:
#       return i+1


# some(arr)

## minimum element in rotated sorted array

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # If array has only one element
        if len(nums) == 1:
            return nums[0]
            
        # If array is not rotated (already sorted)
        if nums[0] < nums[-1]:
            return nums[0]
            
        # Find the pivot point (minimum element)
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                return nums[i+1]
        
        # If no pivot found (shouldn't reach here for valid input)
        return nums[0]