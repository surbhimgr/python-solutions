import math
t=int(input())
j=1
def isprime(n):
    if n%2==0 and n!=2:
        return 0
    m=int(math.sqrt(n))
    for i in range(3,m+1,2):
        if n%i==0:
            return 0
            break
    return 1
        
while t!=0:
    z=int(input())
    p=0
    pre=2
    k=0
    for i in range(z):
        if isprime(i):
            p=k
            k=pre*i
            if k>z:
                break
            pre=i
            
    
    print("Case #"+str(j)+":",p)
    j+=1
    t-=1
