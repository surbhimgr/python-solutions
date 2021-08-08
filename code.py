class Solution:
    def makeFancyString(self, s: str) -> str:
        ans=[]
        n=len(s)
        cnt=1
        ans.append(s[0])
        for i in range(1,n):
            if s[i]==s[i-1]:
                cnt+=1
                if cnt<3:
                    ans.append(s[i])
            else:
                cnt=1
                ans.append(s[i])
        res=""
        return res.join(ans)