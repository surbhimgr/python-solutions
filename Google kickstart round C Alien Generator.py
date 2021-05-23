import math
t=int(input())
j=1
while t!=0:
    g=int(input())
    cnt=0
    s=int(g/2)+1
    for n in range(1,2*g):
        k=((2*g)-(n*n)+n)/(2*n)
        if k<1:
            break
        if k>=1 and k.is_integer():
            cnt+=1
    print("Case #"+str(j)+":",cnt)
    j+=1
    t-=1