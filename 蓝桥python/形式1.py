start=[1 if i=='*' else -1 for i in input()]##这种形式
end=[1 if i=='*' else -1 for i in input()]
n=len(start)
count=0
for i in range(n-1):
    if start[i]!=end[i]:
        count+=1
        start[i]*=-1
        start[i+1]*=-1
print(count)