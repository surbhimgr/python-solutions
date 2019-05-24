t = int(input())
while t!=0 :
    n = int(input())
    if n!=0 and (n & (n-1) == 0) :
        print("True")
    else :
        print("False")
    t+=-1