t = int(input())
l1 = []
l2 = []
sum1 = 0
sum2 = 0
while t!=0 :
    a, b = map(int, input().split())
    sum1+=a
    sum2+=b
    p = 1 if sum1-sum2>0 else 2
    d = sum1-sum2 if sum1-sum2>0 else sum2-sum1
    l1.append(d)
    l2.append(p)
    t+=-1
m = max(l1)
k = l1.index(m)
print(l2[k],m)


