class Solution:
    def nextGreaterElement(self, nums1, nums2):

        stack = []
        nge = {}

        for num in reversed(nums2):

            while stack and stack[-1] <= num:
                stack.pop()

            if stack:
                nge[num] = stack[-1]
            else:
                nge[num] = -1

            stack.append(num)

        ans = []

        for num in nums1:
            ans.append(nge[num])

        return ans