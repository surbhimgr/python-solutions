t = int(input())
while t!=0 :
    n = int(input())
    ar = list(map(int, input().split()))
    ar.sort()
    if len(ar)!=n+1 :
        ar.append(0)
    for i in range(n+2) :
        if ar[i]!=i+1 :
            print(i+1)
            break
    t+=-1

# t = int(input())
# while t!=0 :
#     n = int(input())
#     sum1 = 0
#     ar = list(map(int, input().split()))
#     for i in ar :
#         sum1 = sum1 + i
#     print(sum1)
#     sum2 = ((n+1)*(n+2))/2
#     print(sum2)
#     print(int(sum2-sum1))
#     t+=-1