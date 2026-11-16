class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a=sorted(strs)
        ans=""
        f=a[0]
        l=a[-1]
        for i in range(min(len(f),len(l))):
            if f[i]!=l[i]:
                return ans
            ans+=f[i]
        return ans
        