#we have dictionary of items, a sorting parameter and sorting order. 
#If sorting parameter is 0 then we sort the dictionary according to keys of dictionary, if it is 1 then we sort it according to value at index 0 and if it is 2 then we sort it acc to value at index 1.
#if sorting order is 0 then sort in ascending order and if sorting order is 1 then sort in descending order.
#Then we assume the items are present in some pages, the page no. is given and items per page is also given and we have to print the items on that particular page no.

d={"i4":[302,408],"i1":[982,234],"i2":[452,236],"i3":[564,782]}
pageNo=2
itemsPerPage=3
sortingParamenter=2
sortingOrder=1
arr=[]

pgn=pageNo
ipp=itemsPerPage
sp=sortingParamenter
so=sortingOrder
if sp==0:
    for key in sorted(d.keys()):
        arr.append(key)
    if so==1:
        arr=arr[::-1]
elif sp==1:
    for key in sorted(d.items(), key =lambda kv:(kv[1], kv[0])):
        arr.append(key)
    if so==1:
        arr=arr[::-1]
else:
    for key in sorted(d.items(), key =lambda kv:(kv[1][1], kv[0][1])):
        arr.append(key)
    if so==1:
        arr=arr[::-1]
              
k=0
for i in range(pgn):
    for j in range(ipp):
        if i==pgn-1:
            if k<len(arr):
                print(arr[k])
        k+=1