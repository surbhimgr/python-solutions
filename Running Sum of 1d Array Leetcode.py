class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        pre=0
        ans=0
        l=[]
        for i in nums:
            ans=pre+i
            l.append(ans)
            pre=ans
        return l
