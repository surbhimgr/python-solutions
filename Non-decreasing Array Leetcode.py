import random
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n=len(nums)
        cnt=0
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                cnt+=1
                if cnt==2:
                    return False
                    break
                if i==0:
                    nums[i]=nums[i+1]-1
                elif i+1==n-1:
                    nums[i+1]=nums[i]+1
                else:
                    t=nums[i]
                    nums[i]=nums[i+1]
                    if nums[i]<nums[i-1]:
                        nums[i+1]=t
                        nums[i]=t

        return True
                