class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[-1]*(n+1) for _ in range(m+1)]
        return self.f(m-1,n-1,obstacleGrid,dp)

    def f(self,m,n,grid,dp):
        if m>=0 and n>=0 and grid[m][n]==1:
            return 0
        if m==0 and n==0:
            return 1
        if m<0 or n<0:
            return 0
        if dp[m][n]!=-1:
            return dp[m][n]
        up=self.f(m-1,n,grid,dp)
        l=self.f(m,n-1,grid,dp)
        dp[m][n]=up + l
        return dp[m][n]