class Solution(object):
    
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MAX_STEP = 10001

        n = len(nums)
        if n == 1:
            return 0

        steps = [0 for _ in range(n)]
        for idx in range(n - 2, -1, -1):
            # can reach index n - 1 from here in one leap
            if idx + nums[idx] >= n - 1:
                steps[idx] = 1
                continue
            min_step = MAX_STEP
            for jump_len in range(1, nums[idx] + 1):
                if steps[idx + jump_len] != 0:
                    min_step = min(min_step, 1 + steps[idx + jump_len])
            if min_step != MAX_STEP:
                steps[idx] = min_step
        
        print(steps)

        return steps[0]
        


sol = Solution()

nums = [1,2,3]

res = sol.jump(nums)

print(res)