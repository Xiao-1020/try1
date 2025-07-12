def judge(m):
    for i in res:
        if i[0]//m>i[1]:
            return -1
        elif i[0]//m<i[1]:
            return 1
    return 0


def find_min(min_num,lst):
    i,j=-1,min_num
    while i+1!=j:
        m=(i+j)//2
        if judge(m)==1:
            j=m
        elif judge(m)==-1:
            i=m
        elif judge(m)==0:
            mix=m
            j=m
    return mix


def find_max(min_num,lst):
    i,j=-1,min_num
    while i+1!=j:
        m=(i+j)//2
        if judge(m)==1:
            j=m
        elif judge(m)==-1:
            i=m
        elif judge(m)==0:
            mx=m
            i=m
    return mx
        

N=int(input())
min_num=float('-inf')
res=[]
for i in range(N):
    a,b=map(int,input().split())
    min_num=max(min_num,a)
    res.append((a,b))
print(find_min(min_num,res),find_max(min_num,res))