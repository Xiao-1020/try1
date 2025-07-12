def find(a):
    if father[a]!=a:
        father[a]=find(father[a])
    return father[a]

def union(a,b):
    father[find(b)]=find(a)

m,n=map(int,input().split())
father={a:a for a in range(1,m*n+1)}
k=int(input())
count=0
for i in range(k):
    a,b=map(int,input().split())
    if find(a)!=find(b):
        union(a,b)
        count+=1
print(m*n-count)