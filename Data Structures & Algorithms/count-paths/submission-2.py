class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1]*(n+1) for _ in range(m+1)]
        return self.f(m-1,n-1,dp)
    

    def f(self,i,j,dp):
        if i==0 and j==0:
            return 1
        if i <0 or j<0:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        up=self.f(i-1,j,dp)
        l=self.f(i,j-1,dp)
        dp[i][j]=up+l
        return dp[i][j]
        