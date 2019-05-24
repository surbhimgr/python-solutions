t=int(input());
for i in range(t) :
    n1, n2 = map(int, input().split( ))
    n1s = str(n1)
    n2s = str(n2)
    n1r = int(str(n1s[::-1]))
    n2r = int(str(n2s[::-1]))
    r =  n1r + n2r
    print (r)
