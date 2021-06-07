class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        nums=set(nums)
        nums=list(nums)
        nums.sort()
        m=0
        cnt=1
        n=len(nums)
        for i in range(n-1):
            if nums[i+1]==nums[i]+1:
                cnt+=1
            else:
                m=max(m,cnt)
                cnt=1
        m=max(m,cnt)
        return m