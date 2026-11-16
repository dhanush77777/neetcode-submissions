class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l=0
        mx=0
        ss=set()
        for r in range(len(s)):
            while s[r] in ss:
                ss.remove(s[l])
                l+=1
            ss.add(s[r])
            mx=max(mx,r-l+1)
        return mx
            
