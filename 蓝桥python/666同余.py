N,K=map(int,input().split())
res={}
num=0
for i in range(N):
    num+=int(input())
    leaving=num%K
    res[leaving]=res.get(leaving,0)+1
count=res.get(0,0)
for val in res.values():
    count+=val*(val-1)//2
print(count)