#Determine Whether Matrix Can Be Obtained By Rotation
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        cnt=0
        if target==mat:
            return True
        cmat=mat
        n=len(mat[0])
        while cnt!=3:
            for i in range(n//2):
                for j in range(i, n-i-1):
                    temp=cmat[i][j]
                    cmat[i][j]=cmat[n-1-j][i]
                    cmat[n-1-j][i]=cmat[n-1-i][n-1-j]
                    cmat[n-1-i][n-1-j]=cmat[j][n-1-i]
                    cmat[j][n-1-i]=temp
            if cmat==target:
                return True 
                break
            cnt+=1
        return False
