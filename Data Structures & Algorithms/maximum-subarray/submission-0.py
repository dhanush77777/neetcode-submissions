class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=0
        mx=nums[0]
        for i in nums:
            if curr<0:
                curr=0
            curr+=i
            mx=max(mx,curr)
        return mx
        