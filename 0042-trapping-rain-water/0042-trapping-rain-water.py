class Solution:
    def trap(self, height):

        left = 0
        right = len(height) - 1

        max_left = 0
        max_right = 0

        water = 0

        while left <= right:

            if height[left] <= height[right]:

                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    water += max_left - height[left]

                left += 1

            else:

                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    water += max_right - height[right]

                right -= 1

        return water