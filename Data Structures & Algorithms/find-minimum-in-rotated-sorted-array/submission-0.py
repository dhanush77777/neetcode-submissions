class Solution:
    def findMin(self, nums: List[int]) -> int:
        minn=nums[0]
        l,r=0,len(nums)-1
        while l <=r:
            if nums[l] < nums[r]:
                minn=min(minn,nums[l])
                break
            
            m=(l+r)//2
            minn=min(minn,nums[m])
            if nums[m]>=nums[l]:
                l=m+1
            else:
                r=m-1
        return minn
        