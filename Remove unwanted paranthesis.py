s="((())(()"
n=len(s)
l=[]
k=[]
for i in range(n):
    if s[i]=="(":
        k.append(s[i])
        l.append(i)
    elif s[i]==")" and len(l)!=0:
        k.pop()
        l.pop()
    else:
        l.append(i)
ans=""
for i in range(n):
    if i not in l:
        ans+=s[i]
print(ans)
