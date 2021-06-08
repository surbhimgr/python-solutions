class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        mincost=[0]*(n+1)
        for i in range(2,n+1):
            step1=mincost[i-1]+cost[i-1]
            step2=mincost[i-2]+cost[i-2]
            mincost[i]=min(step1,step2)
        return mincost[-1]