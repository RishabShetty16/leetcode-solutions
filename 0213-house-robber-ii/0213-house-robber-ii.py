class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        def rob_linear(arr):
            n=len(arr)
            if n==1:
                return arr[0]
            dp=[0]*n
            dp[0]=arr[0]
            dp[1]=max(arr[0],arr[1])
            for i in range(2,n):
                skip=dp[i-1]
                take=arr[i]+dp[i-2]
                dp[i]=max(skip,take)
            return dp[-1]

        case1=rob_linear(nums[1:])
        case2=rob_linear(nums[:-1])
        return max(case1,case2)
        