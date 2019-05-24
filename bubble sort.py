t=int(input())
while t!=0 :
    n = int(input())
    cnt=0
    ar = list(map(int, input().split()))
    for i in range(len(ar)) :
        for j in range(len(ar)-i-1) :
            if ar[i]>ar[j] :
                ar[i], ar[j] = ar[j], ar[i]
                cnt+=1
    print(*ar)
    print(cnt)
    t+=-1