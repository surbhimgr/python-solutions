mem=[1,2,3,4,1,2,5,1,2,3,4,5]
k=3
arr=mem[:k]
n=len(mem)
cnt=0
for i in range(k,n):
    if arr[-1]!=mem[i]:
        if mem[i] in arr:
            arr.remove(mem[i])
            arr.append(mem[i])

        else:
            arr.pop(0)
            arr.append(mem[i])
            cnt+=1

print(cnt)

        
