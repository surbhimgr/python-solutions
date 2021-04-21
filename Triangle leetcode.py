#I took reference from youtube where bottom-up approach was used 

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        if len(triangle)==1:
            return triangle[0][0]
        n=len(triangle)
        c=triangle[-1]
        for i in range(n-2,-1,-1):
            for j in range(i+1):
                c[j]=min(c[j],c[j+1])+triangle[i][j]
        return c[0]