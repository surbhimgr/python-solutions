class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cnt=0
        k=capacity
        for i in range(len(plants)):
            if k>=plants[i]:
                cnt+=1
                k=k-plants[i]
            else:
                cnt+=(i+i+1)
                k=capacity
                k=k-plants[i]
        return cnt
        
