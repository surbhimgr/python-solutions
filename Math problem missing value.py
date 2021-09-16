# Program to print missing value from expression
import operator
d={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
d2={'+':'-','-':'+','*':'/','/':'*'}
s="100 * 2 = x00"
n=len(s)
for i in range(n):
    if s[i]==" ":
        n1=s[:i]
        op=s[i+1]
        t=i
        break
for i in range(t+2,n):
    if s[i]==" ":
        n2=s[t+3:i-1]
        n3=s[i+1:]
print(n1,n2,n3)
if 'x' in n1:
    a=d[d2[op]](int(n3),int(n2))
    ix=n1.index('x')
elif 'x' in n2:
    ix=n2.index('x')
    if op=='+' or op=='*':
        a=d[d2[op]](int(n3),int(n1))
    else:
        a=d[op](int(n1),int(n3))
elif 'x' in n3:
    ix=n3.index('x')
    a=d[op](int(n1),int(n2))
else:
    a="="
if a!='=':
    ans=list(map(int,str(int(a))))
    x=ans[ix]
    print(x)
else:
    print(a)
    
    
