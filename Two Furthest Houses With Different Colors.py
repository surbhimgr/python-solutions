class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        a=colors[0]
        for i in range(len(colors)-1,-1,-1):
            if a!=colors[i]:
                a=i
                break
        b=colors[-1]
        for i in range(len(colors)):
            if b!=colors[i]:
                b=len(colors)-i-1
                break
        return max(a,b)
        
