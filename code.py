class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=[]
        if target not in nums:
            return [-1,-1]
        l.append(nums.index(target))
        nums.reverse()
        l.append(len(nums)-nums.index(target)-1)
        return l