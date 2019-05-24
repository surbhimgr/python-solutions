t = int(input())
while t!=0 :
    n = int(input())
    i = 5
    cnt = 0
    if n==0 :
        print(0)
    else:
        while n/i>=1 :
            cnt = cnt + n/i
            i*=5
        print(int(cnt))
    t+=-1
