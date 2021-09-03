class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        s=[False]*n
        for num in nums:
            l=0
            while not s[num]:
                s[num]=True
                l+=1
                num=nums[num]
            ans=max(ans,l)
        return ans
        