cnt=0
def ispalindrome(s):
    if s==s[::-1]:
        return True
def toString(List):
    return ''.join(List)
def allLexicographicRecur (s2, data, last, index,s1):
    global cnt
    length = len(s2)
    for i in range(length):
        data[index] = s2[i]
        if index==last:
            s=toString(data)
            if ispalindrome(s) and s<s1:
                #print("true",s)
                cnt+=1
        else:
            allLexicographicRecur(s2, data, last, index+1,s1)
def allLexicographic(s2,s1):
    length = len(s1)
    data = [""] * (length+1)
    s2 = sorted(s2)
    allLexicographicRecur(s2, data, length-1, 0,s1)
t=int(input())
j=1
alpha='abcdefghijklmnopqrstuvwxyz'
while t!=0:
    cnt=0
    n,k=map(int,input().split())
    
    s1 = input()
    s2=alpha[0:k]
    #print ("All permutations with repetition of " + s2 + " are:")
    allLexicographic(s2,s1)
    print("Case #"+str(j)+":",cnt)
    t-=1
    j+=1

