n, k = map(int, input().split())
l1 = list(map(int, input().split()))
m = int(input())
sum1=0
for i in l1:
    sum1=sum1+i
sum2=(sum1-l1[k])/2
if (sum2)==m:
    print("Bon Appetit")
else :
   print(int(m-(sum2)))
