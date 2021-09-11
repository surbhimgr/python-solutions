arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n=len(arr)
arr.sort()
dep.sort()
pl=0
ans=0
i=0
j=0
while i<n and j<n:
    if arr[i]<dep[j]:
        pl+=1
        i+=1
    else:
        pl-=1
        j+=1
    ans=max(ans,pl)
print(ans)