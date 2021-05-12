t = int(input())
while t!=0 :
    xyz = input().split()
    x = int(xyz[0])
    y = int(xyz[1])
    z = int(xyz[2])
    d1 = x-z if x>z else z-x
    d2 = y-z if y>z else z-y
    if d1>d2 :
        print("Cat B")
    elif d1<d2 :
        print("Cat A")
    else :
        print("Mouse C")
    t+=-1
