class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1 or n==2:
            return 0
        p=[True for i in range(n+1)]
        k=2
        while k*k<=n:
            if p[k]==True:
                for j in range(k*2,n+1,k):
                    p[j]=False
            k+=1
        p[0]=False
        p[1]=False
        cnt=0
        for t in range(n):
            if p[t]:
                cnt+=1
        return cnt