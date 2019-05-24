t = int(input())
while t!=0 :
    st = input()
    l1=[]
    if len(st)>10 :
        l1.append(st[0])
        l1.append(len(st)-2)
        l1.append(st[len(st)-1])
        print(*l1,sep="")
    else :
        print(st)
    t+=-1

# l1 = list(map(int, input().split()))
# a1 = l1[0] * l1[1]
# a2 = l1[2]**2
# i = 1
# m1 = 0
# while m1<a1 :
#     m1=m1+a2
#     i+=1
# print(i)