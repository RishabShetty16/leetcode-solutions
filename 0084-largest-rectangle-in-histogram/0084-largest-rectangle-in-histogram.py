class Solution:
    def largestRectangleArea(self, heights):

        n = len(heights)

        stack = []

        leftsmall = [0] * n
        rightsmall = [0] * n

        # Nearest Smaller to Left (NSL)
        for i in range(n): 

            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if not stack:
                leftsmall[i] = 0
            else:
                leftsmall[i] = stack[-1] + 1

            stack.append(i)

        stack.clear()

        # Nearest Smaller to Right (NSR)
        for i in range(n - 1, -1, -1):

            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if not stack:
                rightsmall[i] = n - 1
            else:
                rightsmall[i] = stack[-1] - 1

            stack.append(i)

        maxArea = 0

        for i in range(n):

            width = rightsmall[i] - leftsmall[i] + 1
            area = heights[i] * width

            maxArea = max(maxArea, area)

        return maxArea  