t=int(input())
j=1
while t!=0:
    n=int(input())
    l=list(map(int,input().split()))
    s=set(l)
    p=list(s)
    p.sort()
    print(l)
    print(s)
    print(p)
    cnt=0
    k=1
    ans=0
    for i in p:

        ans+=(l.count(i)*k)
        k+=1
        print(i,ans,k)    
    
    
    print("Case #"+str(j)+": ",ans)
    j+=1
    t-=1
