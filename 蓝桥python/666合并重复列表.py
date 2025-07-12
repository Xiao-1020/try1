l,n=map(int,input().split())
area=[]
for i in range(n):
    area.append(list(map(int,input().split())))
area.sort(key=lambda x:x[0])
i=0
remove_list=[]
while i<n-1:
    if area[i+1][0]<area[i][1]:
        if area[i+1][1]<=area[i][1]:
            area[i+1][0]=area[i][0]
            area[i+1][1]=area[i][1]
            remove_list.append(i)
        else:
            area[i+1][0]=area[i][0]
            remove_list.append(i)
    i+=1
remove_list=remove_list[::-1]
for i in remove_list:
    area.pop(i)
total=0
for i in area:
    total+=int(i[1])-int(i[0])+1
print(l-total+1)