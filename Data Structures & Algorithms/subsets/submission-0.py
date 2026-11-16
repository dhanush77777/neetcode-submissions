class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ds,ans=[],[]
        self.f(0,ds,ans,len(nums),nums)
        return ans

    def f(self,i,ds,ans,n,a):
        if i ==n:
            ans.append(list(ds))
            return
        #pick
        ds.append(a[i])
        self.f(i+1,ds,ans,n,a)
        ds.remove(a[i])
        
        self.f(i+1,ds,ans,n,a)
        