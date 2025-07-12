def findcoin(total,coins):
    minnum=total
    if total in coins:
        know_num[str(total)]=1
        return(1)
    elif str(total) in know_num:
        return(know_num[str(total)])
    else:
        for i in [j for j in coins if j<total]:
            num=1+findcoin(total-i,coins)
            if minnum>num:
                minnum=num
                know_num[str(total)]=num
    return(minnum)
coins=[1,5,10,25]
total=int(input())
know_num={}
print(findcoin(total,coins))