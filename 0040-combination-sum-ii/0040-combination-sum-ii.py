from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        ans = []

        def backtrack(index, target, path):

            if target == 0:
                ans.append(path[:])
                return

            for i in range(index, len(candidates)):

                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > target:
                    break

                path.append(candidates[i])

                backtrack(i + 1, target - candidates[i], path)

                path.pop()

        backtrack(0, target, [])

        return ans