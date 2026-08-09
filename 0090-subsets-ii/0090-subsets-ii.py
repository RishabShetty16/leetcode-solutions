from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        ans = []

        def backtrack(index, subset):

            ans.append(subset[:])

            for i in range(index, len(nums)):

                if i > index and nums[i] == nums[i - 1]:
                    continue

                subset.append(nums[i])

                backtrack(i + 1, subset)

                subset.pop()

        backtrack(0, [])

        return ans