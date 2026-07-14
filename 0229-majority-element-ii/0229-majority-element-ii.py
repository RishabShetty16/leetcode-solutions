from collections import defaultdict
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)

        result = []

        mpp = defaultdict(int)

        mini = n // 3 + 1

        for num in nums:
            mpp[num] += 1

            if mpp[num] == mini:
                result.append(num)

            if len(result) == 2:
                break

        return result