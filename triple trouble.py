t = int(input())
while t!=0 :
    n = int(input())
    l1 = list(map(int, input().split()))
    l1.sort()
    l1.append(0)
    for i in range(0,n,3) :
        if l1[i]!=l1[i+1] :
            print(l1[i])
            print("hi")
            break
    t+=-1