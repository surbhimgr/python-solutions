class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[]
        n1=len(word1)
        n2=len(word2)
        for i in range(n1+1):
            temp=[]
            for j in range(n2+1):
                if i==0 or j==0:
                    temp.append(i+j)
                elif word1[i-1]==word2[j-1]:
                    temp.append(dp[j-1])
                else:
                    temp.append(1+min(dp[j],temp[j-1]))
            dp=temp
        return dp[len(word2)]