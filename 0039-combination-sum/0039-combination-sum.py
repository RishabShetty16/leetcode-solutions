from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []
        ds = []

        def backtrack(index, target):

            if target == 0:
                ans.append(ds[:])
                return

            if index == len(candidates):
                return

            if candidates[index] <= target:
                ds.append(candidates[index])

                backtrack(index, target - candidates[index])

                ds.pop()

            backtrack(index + 1, target)

        backtrack(0, target)

        return ans