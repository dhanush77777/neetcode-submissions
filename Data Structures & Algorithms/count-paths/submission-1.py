class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid=[[1]*n for _ in range(m)]
        dp=[[-1]*(n+1) for _ in range(m+1)]
        return self.f(m-1,n-1,grid,dp)
    

    def f(self,i,j,grid,dp):
        if i==0 and j==0:
            return 1
        if i <0 or j<0:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        up=self.f(i-1,j,grid,dp)
        l=self.f(i,j-1,grid,dp)
        dp[i][j]=up+l
        return dp[i][j]
        