class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n=len(questions)
        dp=[0]*(n+1)
        for i in range(n-1,-1,-1):
            points=questions[i][0]
            brainpower=questions[i][1]
            next_question=i+brainpower+1
            skip=dp[i+1]
            solve=points
            if next_question<n:
                solve+=dp[next_question]
            dp[i]=max(solve,skip)
        return dp[0]
        
        