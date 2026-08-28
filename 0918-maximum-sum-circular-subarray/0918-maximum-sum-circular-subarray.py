class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total=sum(nums)
        current_max=nums[0]
        best_max=nums[0]
        current_min=nums[0]
        best_min=nums[0]
        for num in nums[1:]:
            current_max=max(current_max+num,num)
            best_max=max(current_max,best_max)

            current_min=min(current_min+num,num)
            best_min=min(current_min,best_min)

        if best_max <0:
            return best_max
        circular_sum=total-best_min
        return max(best_max,circular_sum)



        