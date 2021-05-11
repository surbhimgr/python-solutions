bnm = input().split()
b = int(bnm[0])
n = int(bnm[1])
m = int(bnm[2])
keyb = list(map(int, input().split()))
dri = list(map(int, input().split()))
maxx=0
for i in keyb:
    for j in dri:
        if i+j>maxx and b>=i+j:
            maxx=i+j
if maxx!=0:
    print(maxx)
else :
    print("-1")




