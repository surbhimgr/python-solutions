arr=[7,-1,2,20,1,3]
n=len(arr)
cnt1=0
if n==0:
    print(":(")
for i in range(n):
    if arr[i]==1:
        cnt1=1
    if arr[i]>n or arr[i]<=0:
        arr[i]=1
if cnt1==0:
    print('1')
for i in range(n):
    ind=abs(arr[i])-1
    if arr[ind]>0:
        arr[ind]=arr[ind]*-1
for i in range(n):
    if arr[i]>0:
        print(i+1)
        break
print(n+1)
