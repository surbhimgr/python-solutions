class Solution:
    def isPossible(self, target: List[int]) -> bool:
        l=len(target)
        if l==1:
            return target==[1]
        mh=[-i for i in target]
        heapq.heapify(mh)
        t=sum(target)
        while -mh[0]>1:
            m=-heapq.heappop(mh)
            r=t-m
            if r==1:
                return True
            x=m%r
            
            if x<1 or x==m:
                return False
            
            heapq.heappush(mh,-x)
            t+=x-m
        return True

        