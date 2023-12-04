class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_h = -1
        max_h_idx = -1
        n = len(height)

        if n <= 2:
            return 0

        water_cnt = 0

        for i in range(n):
            if height[i] > max_h:
                max_h = height[i]
                max_h_idx = i
        
        # print(f"max_h = {max_h}  max_h_idx = {max_h_idx}")
        
        left = 0
        for i in range(1, max_h_idx + 1):
            if height[i] >= height[left]:
                brick_cnt = 0
                for j in range(left + 1, i):
                    brick_cnt += height[j]
                water_cnt += (i - left - 1) * height[left] - brick_cnt
                # print(f"left = {left}  i = {i}  water = {water_cnt}")
                left = i

        # print("half way: ",water_cnt)

        right = n - 1
        for i in range(n - 2, max_h_idx - 1, -1):
            if height[i] >= height[right]:
                brick_cnt = 0
                for j in range(i + 1, right):
                    brick_cnt += height[j]
                water_cnt += (right - i - 1) * height[right] - brick_cnt
                # print(f"i = {i}  right = {right}  water = {water_cnt}")
                right = i

        return water_cnt
    
        # left = 0
        # right = 1
        # max_h = height[1]

        # while right < len(height):
        #     curr_h = height[right]
        #     if curr_h < max_h or curr_h
        #     if height[right] > max_h:
        #         max_h = height[right]

        # pass

sol = Solution()

# height = [0,1,0,2,1,0,1,3,2,1,2,1]

height = [2, 0, 2]

res = sol.trap(height)

print(res)