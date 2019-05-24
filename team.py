t = int(input())
cnt = 0
while t!=0 :
    l1 = list(map(int, input().split()))
    if sum(l1)>=2 :
        cnt+=1
    t+=-1
print(cnt)