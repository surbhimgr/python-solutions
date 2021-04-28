class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==1:
            return 0
        ans=obstacleGrid
        r=len(obstacleGrid)
        c=len(obstacleGrid[0])
        ans[0][0]=1

        for i in range(1,c):
            if obstacleGrid[0][i]==0 and ans[0][i-1]==1:
                ans[0][i]=1
            else:
                ans[0][i]=0
        for j in range(1,r):
            if obstacleGrid[j][0]==0 and ans[j-1][0]==1:
                ans[j][0]=1
            else:
                ans[j][0]=0
        for i in range(1,r):
            for j in range(1,c):
                if obstacleGrid[i][j]==1:
                    ans[i][j]=0
                else:
                    ans[i][j]=ans[i][j-1]+ans[i-1][j]
        return ans[r-1][c-1]
        
