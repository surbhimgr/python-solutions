class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n=len(s)
        cnt=0
        for i in range(n-2):
            t=s[i:i+3]
            if len(t)==len(set(t)):
                cnt+=1
        return cnt
            