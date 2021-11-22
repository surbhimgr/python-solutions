class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        cnt=0
        d=0
        a=[[0,1],[0,-1],[1,0],[-1,0]]
        vi=[[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if vi[i][j]==1 or grid[i][j]=='0':
                    d+=1
                else:
                    vi[i][j]=1
                    cnt+=1
                    q=[]
                    q.append([i,j])
                    while q:
                        x=q[0][0]
                        y=q[0][1]
                        q.pop(0)
                        for k in range(4):
                            x1=x+a[k][0]
                            y1=y+a[k][1]
                            if x1>=0 and x1<m and y1>=0 and y1<n and vi[x1][y1]==0 and grid[x1][y1]=='1':
                                q.append([x1,y1])
                                vi[x1][y1]=1
        
        return cnt
        
