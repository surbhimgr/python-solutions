t=int(input())
j=1
while t!=0:
    n=int(input())
    s=input()
    cnt=1
    l=[1]
    for i in range(1,n):
        if s[i-1]<s[i]:
            cnt+=1
        else:
            cnt=1
        l.append(cnt)
    
    
    print("Case #"+str(j)+":",*l,sep=" ")
    j+=1
    t-=1
