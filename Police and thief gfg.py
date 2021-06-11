arr=['P', 'T', 'T', 'P', 'T']
k=1
def polthe(arr,k):
    pol,the=-1,-1
    n=len(arr)
    ans=0
    for i in range(n):
        if arr[i]=='P':
            pol=i
            break
    for j in range(n):
        if arr[j]=='T':
            the=j
            break
    print(pol,the)
    if pol==-1 or the==-1:
        return 0
    else:
        if abs(i-j)<=k:
            ans+=1
    while pol<n and the<n:
        for i in range(pol+1,n):
            if arr[i]=='P':
                pol=i
            break
        for j in range(the+1,n):
            if arr[j]=='T':
                the=j
            break
        print(pol,the)
        if abs(i-j)<=k:
            ans+=1
    return ans
print(polthe(arr,k))