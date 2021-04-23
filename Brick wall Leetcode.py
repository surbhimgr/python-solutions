class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        dic=defaultdict(int)
        for i in wall:
            cnt=0
            li=len(i)
            for j in range(li-1):
                cnt+=i[j]
                dic[cnt]+=1
        n=len(wall)
        ans=n
        for _,c in dic.items():
            ans=min(ans,n-c)
        return ans