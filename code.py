class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        c=0
        for i in range(n):
            for j in range(c,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
            c+=1
        c=0
        l=n-1
        for j in range(int(n/2)):
            for i in range(n):
                matrix[i][j],matrix[i][l-c]=matrix[i][l-c],matrix[i][j]
            c+=1