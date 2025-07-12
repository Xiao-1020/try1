num=int(input())
lst=list(range(1,int(input())+1))
head=0;tail=len(lst)-1
while head<tail:
    for i in range(num-1):
        lst.append(lst[head])
        head+=1
        tail+=1
    head+=1
print(lst[head])