class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[-1]*(n+1) for _ in range(m+1)]
        return self.f(m-1,n-1,grid,dp)

    def f(self,m,n,grid,dp):
        if m==0 and n==0:
            return grid[m][n]
        if m<0 or n<0:
            return 10**9
        if dp[m][n]!=-1:
            return dp[m][n]
        up=grid[m][n]+self.f(m-1,n,grid,dp)
        l=grid[m][n]+self.f(m,n-1,grid,dp)
        
        dp[m][n]=min(up,l)
        return dp[m][n]
        