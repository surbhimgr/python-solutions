n = int(input())
p = list(map(int, input().split()))
for i in range(1,n+1) :
    k=p.index(i)+1
    print(p.index(k)+1)

