class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hm={}
        for i in range(len(numbers)):
            tmp=target-numbers[i]
            if tmp in hm:
                return [hm[tmp],i+1]
            hm[numbers[i]]=i+1
        return []
        