n=input()
l1= list(map(int, input().split()))
s=l1[0]
l=l1[0]
cs=0
cl=0
for i in l1:
    if i>l :
        cl+=1
        l=i
    elif i<s:
        cs+=1
        s=i
    else:
        1+1
print(cl, cs)

