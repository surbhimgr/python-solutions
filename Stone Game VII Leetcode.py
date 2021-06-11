class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        l=len(stones)
        ps={-1:0}
        for i,s in enumerate(stones):
            ps[i]=ps[i-1]+s
        dp=[[0]*l for _ in range(l)]
        for j in range(2,l+1):
            for k in range(l-j+1):
                r=k+j-1
                dp[k][r]=max(ps[r]-ps[k]-dp[k+1][r],ps[r-1]-ps[k-1]-dp[k][r-1])
        return dp[0][l-1]