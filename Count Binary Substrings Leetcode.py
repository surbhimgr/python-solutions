class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        pcnt=0
        ccnt=1
        cnt=0
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                ccnt+=1
            if s[i]!=s[i+1]:
                if pcnt>0:
                    cnt+=min(pcnt,ccnt)
                    pcnt=ccnt
                    ccnt=1
                else:
                    pcnt=ccnt
                    ccnt=1
            if i==len(s)-2:
                cnt+=min(pcnt,ccnt)
                
            
        return cnt
            
        