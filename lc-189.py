class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # Try this: Could you do it in-place with O(1) extra space?
        n = len(nums)
        k = k % n
        tmp = nums[: n - k]
        nums[: k] = nums[-k: ]
        nums[k: ] = tmp

sol = Solution()

arr = [1,2,3,4,5,6,7]

sol.rotate(arr, 10)

print(arr)