from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(c):
            v[c]=True
            for j in d[c]:
                if v[j]!=True:
                    dfs(j)
            return

        n=len(isConnected)
        v=[False]*n
        stack=[]
        cnt=0
        d=defaultdict(list)
        for i in range(n):
            for j in range(len(isConnected[i])):
                if isConnected[j][i] and i!=j:
                    d[i].append(j)
        cnt+=(n-len(d))
        for i in d:
            if v[i]!=True:
                cnt+=1
                dfs(i)
                

        return cnt

                
