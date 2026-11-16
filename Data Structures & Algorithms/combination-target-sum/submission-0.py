class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        ds=[]
        i=0
        self.f(i,ds,target,ans,nums)
        return ans

    def f(self,i,ds,t,ans,a):
        if i==len(a):
            if t==0:
                ans.append(list(ds))
            return
        #pick condition
        if a[i]<=t:
            ds.append(a[i])
            self.f(i,ds,t-a[i],ans,a)
            ds.remove(a[i])
        #not pick condition
        self.f(i+1,ds,t,ans,a)

        