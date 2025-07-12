stack=[]
s=input()
top=-1
s1=["(","[","{"]
s2=[")","]","}"]
balanced=True
for i in s:
    if i in s1:
        top+=1
        stack.append(i)
    elif i in s2:
        if top<0:
            balanced=False
            break
        elif top>0 and s1.index(stack[top])!=s2.index(i):
            balanced=False
            break
        else:
            stack.pop(top)
            top-=1
if balanced==True and top==-1:
    print("YES")
else:
    print("No")