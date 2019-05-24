t = int(input())
while t!=0 :
    n = int(input())
    a = list(map(int, input().split()))
    l1 = []
    for i in range(len(a)):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        l1.append(i)
        l1.append(min_idx)
    print(*l1)
    print(*a)
    t+=-1