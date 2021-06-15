class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        @lru_cache(None)
        def fun(mask,sr,cur):
            if sr==0 and mask==0:
                return True
            for i in range(n):
                if mask & (1<<i)!=0:
                    if matchsticks[i]<=cur:
                        nr=cur-matchsticks[i]
                        if fun(mask^(1<<i), sr if nr else sr-1, ml if not nr else nr):
                            return True
            return False

        s=sum(matchsticks)
        if s%4:
            return False
        ml=s//4
        n=len(matchsticks)


        return fun((1<<n)-1,4,ml)


                        
            
        
