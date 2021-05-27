class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n=len(words)
        m=0
        cn=0
        for i in range(n-1):
            for j in range(i+1,n):
                for c in words[i]:
                    if c in words[j]:
                        cn=1
                        break
                if cn==0:
                    il=len(words[i])
                    ij=len(words[j])
                    m=max(m,il*ij)
                cn=0
        return m