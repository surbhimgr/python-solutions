t = int(input())
while t!=0 :
    a, b = map(int, input().split())
    p = int(input())
    l1=[]
    l2=[]
    while p>0 :
        m, n = map(int, input().split())
        l1.append(m)
        l2.append(n)
        p += -1
    if a>b :
        a, b = b, a
    sum1 = sum(l1)
    sum2 = sum(l2)
    if sum1>sum2 :
        l1=[x*a for x in l1]
        l2=[y*b for y in l2]
    else:
        l2=[x*a for x in l2]
        l1=[y*b for y in l1]
    print(sum(l1)+sum(l2))
    t+=-1

