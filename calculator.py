def add(var1,var2):
     print("output is",var1+var2)
def sub(var1,var2):
    print("output is",var1-var2)
def mul(var1,var2):
    print("output is",var1*var2)
def div(var1,var2):
     print("output is",var1/var2)
def sqr(var1):
    import math
    print("output is",math.sqrt(var1))
i=1
while i!=0:
    print("""the following operations can performed by the calculator
                1.addition
                2.substraction
                3.multiplication
                4.division
                5.square root""")
    op=int(input("please enter the operation to be performed or else type 0 to exit"))

    try :
        if op==1:
            n1=int(input("please enter a number "))
            n2 = int(input("please enter another number "))
            add(n1,n2)

        elif op == 2:
            n1 = int(input("please enter a number "))
            n2 = int(input("please enter another number "))
            sub(n1, n2)

        elif op == 3:
            n1 = int(input("please enter a number "))
            n2 = int(input("please enter another number "))
            mul(n1, n2)

        elif op == 4:
            n1 = int(input("please enter a number "))
            n2 = int(input("please enter another number "))
            div(n1, n2)

        elif op == 5:
            n1 = int(input("please enter a number "))
            sqr(n1)
        elif op ==0 :
            i=0
        else :
            print("invalid input")
    except ValueError:
        print("please provide input as int")