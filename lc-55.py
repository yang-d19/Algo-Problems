class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        far_pos = nums[0]
        for i in range(n):
            if i <= far_pos:
                far_pos = max(far_pos, i + nums[i])
            else:
                return False
            
            if far_pos >= n - 1:
                return True


sol = Solution()   

res = sol.canJump([3,2,1,0,4])

print(res)