def hit(int input1, str input2):
    m=0
    cnt=0
    for i in range(input1):
        if input2[i]=="h":
            cnt+=1
            if input2[i+1]!="h" and input2[i+1]!="i":
                cnt=0
        if input2[i]=="i" and cnt>0:
            cnt+=1
            if input2[i+1]!="i" and input2[i+1]!="t":
                cnt=0
        if input2[i]=="t" and cnt>0:
            cnt+=1
            if i==input1-1:
                m=max(m,cnt)
            else:
                if input2[i+1]!="t":
                    m=max(m,cnt)
                    cnt=0
    return m
        
        
