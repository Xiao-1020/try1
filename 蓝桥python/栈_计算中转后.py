line={"*":3,"/":3,"+":2,"-":2,"(":1}
s=input()
stack=[]
top=-1
num="1234567890"
ways="+-*/"
result=''
for i in s:
    if i in num:
        result+=i
    elif i=="(":
        top+=1
        stack.append(i)
    elif i==")":
        while True:
            remove=stack.pop()
            top-=1
            if remove=="(":
                break
            else:
                result+=remove
    elif i in ways:
        if top>=0 and line[stack[-1]]>=line[i]:
            remove=stack.pop()
            top-=1
            result+=remove
            stack.append(i)
            top+=1
        elif top==-1:
            top+=1
            stack.append(i)
        else:
            stack.append(i)
            top+=1
while top>=0:
    remove=stack.pop()
    result+=remove
    top-=1
print(result) 