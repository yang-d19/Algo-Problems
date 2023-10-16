class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = [0 for i in range(len(nums))]
        arr[0] = nums[0]

        # Initialize the max sum
        max_sum = arr[0]
        # Traverse all the element through the loop
        for i in range(1, len(nums)):
            # arr[i] represents the largest sum of all subarrays ending with index i
            arr[i] = max(arr[i-1] + nums[i], nums[i])
            # if arr[i] > maxSum then maxSum = arr[i].
            if arr[i] > max_sum:
                max_sum = arr[i]

        return max_sum    