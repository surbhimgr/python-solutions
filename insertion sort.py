t = int(input())
while t!=0 :
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(1,n) :
        key = a[i]
        j = i-1
        while j>=0 and key < a[j] :
            a[j+1] = a[j]
            j-=1
        a[j+1] = key
        print(j+1)