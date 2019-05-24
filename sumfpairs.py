import sys
# t=int(input())
# for p in range(t) :
#     n, k = map(int, input().split())
#     c=0
#     arr = list(map(int, input().split()))
#     arr.sort()
#     s=0
#     l=len(arr)-1
#     while s < l :
#             if arr[s] + arr[l]==k :
#                 c=1
#                 break
#             elif  arr[s] + arr[l] < k :
#                 s+=1
#             else :
#                 l+=-1
#     print(c)
#     if c==1 :
#         print("True")
#     else :
#         print("False")
#
# t=int(input())
# for p in range(t) :
#     n, k = map(int, input().split())
#     c=0
#     arr = list(map(int, input().split()))
#     arr.sort()
#     s=0
#     l=len(arr)-1
#     while s < l :
#             if k-(arr[s] + arr[l]) in arr :
#                 c=1
#             elif k-(arr[s] + arr[l]) < k :
#                 s+=1
#             else :
#                 l+=-1

n=int(input())
arr = list(map(int, input().split()))
arr.sort()
t=int(input())
for p in range(t) :
    c=0
    k = int(input())
    d1 = k-arr
    if arr[n/2]<=k :
        for i in range(n/2,-1,-1) :
            if arr[i]<=k :
                c=1
                a=arr[i]
                break
    if c==1 :
        print(a)
    else:
        print("-2147483648")
