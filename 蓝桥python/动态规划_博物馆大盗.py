bw=[None,{'w':2,'v':3},{'w':3,'v':4},{'w':4,'v':8},{'w':5,'v':8},{'w':9,'v':10}]
m=int(input())
maxvalue=[]
for i in range(len(bw)):
    new=[]
    for j in range(m+1):
        new.append(0)
    maxvalue.append(new)#注意创建二位列表的格式
for i in range(len(bw)):
    for j in range(m+1):
        if i==0 or j==0:
            maxvalue[i][j]=0
        elif bw[i]['w']>j:
            maxvalue[i][j]=maxvalue[i-1][j]
        else:
            maxvalue[i][j]=max(maxvalue[i-1][j-bw[i]['w']]+bw[i]['v'],maxvalue[i-1][j])
print(maxvalue[len(bw)-1][m])