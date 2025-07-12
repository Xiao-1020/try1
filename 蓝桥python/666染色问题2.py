def dye(current,colournum):
    global minnum
    if colournum>=minnum:
        return
    if current>n:
        minnum=min(minnum,colournum)
        return
    for i in range(1,colournum+1):
        k=0
        while room[i][k]!=0 and familar[current][room[i][k]]==0:
            k+=1
        if room[i][k]==0:
            room[i][k]=current
            dye(current+1,colournum)
            room[i][k]=0
    room[colournum+1][0]=current
    dye(current+1,colournum+1)
    room[colournum+1][0]=0

n=int(input())
m=int(input())
familar=[[0]*(n+1) for i in range(n+1)]
minnum=n
room=[[0]*(n+1) for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    familar[a][b]=1
    familar[b][a]=1
dye(1,1)
print(minnum)