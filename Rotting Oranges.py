class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        rotor=[]
        fror=0
        timer=0
        neigh=[[0,1],[0,-1],[1,0],[-1,0]]
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    fror+=1
                elif grid[i][j]==2:
                    rotor.append([i,j])
        inlen=len(rotor)
        if fror==0:
            return 0
        while rotor:
            s=rotor.pop(0)
            for k in range(4):
                x1=s[0]+neigh[k][0]
                y1=s[1]+neigh[k][1]
                if x1>=0 and x1<n and y1>=0 and y1<m and grid[x1][y1]==1:
                    grid[x1][y1]=2
                    rotor.append([x1,y1])
                    fror-=1
            inlen-=1
            if inlen==0:
                timer+=1
                inlen=len(rotor)
        if fror==0:
            return timer-1
        else:
            return -1
            
        
        
