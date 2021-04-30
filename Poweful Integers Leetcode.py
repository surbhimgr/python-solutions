class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        a=bound if x==1 else int(log(bound,x))
        b=bound if y==1 else int(log(bound,y))
        
        ans=set([])
        
        for i in range(a+1):
            for j in range(b+1):
                v=x**i + y**j
                if v<=bound:
                    ans.add(v)
                if y==1:
                    break
            if x==1:
                break
        return list(ans)
        