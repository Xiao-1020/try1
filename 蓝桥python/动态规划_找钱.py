def changecoin(total,coins):
    mincoins=[0]*(total+1)
    newchange=[[]]*(total+1)
    for i in range(1,total+1):
        if i in coins:
            mincoins[i]=1
            newchange[i]=[i]
        else:
            newcoins=i
            prechange=[]
            for j in [x for x in coins if x <=i]:
                if mincoins[i-j]!=0 and newcoins>=mincoins[i-j]+1:
                    newcoins=mincoins[i-j]+1
                    prechange=newchange[i-j]
                    new=j
            mincoins[i]=newcoins
            newchange[i]=prechange+newchange[new]
    return (str(mincoins[total]),str(newchange[total]))
total=int(input())
coins=[1,5,10,21,25]
print(",".join(changecoin(total,coins)))