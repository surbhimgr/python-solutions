while True:
    num=int(input("please enter a number :"))
    count=0
    i=num-1
    while i!=0 :
        j=num%i
        if j==0:
            count=count+1
        i=i-1
    if count==1 :
        print("number is prime")
    else :
        print("number is not prime")

