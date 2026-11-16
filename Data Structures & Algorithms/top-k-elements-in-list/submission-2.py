class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        s=Counter(nums)
        sr=sorted(s,key=s.get,reverse=True)
        return sr[:k]
        