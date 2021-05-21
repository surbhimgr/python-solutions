n = int(input())
ar = list(map(int, input().split()))
ar.sort()
cnt=0
i=0
while i<n-1 :
    if ar[i]==ar[i+1] :
        cnt+=1
        i+=2
    else :
        i+=1
print(cnt)

