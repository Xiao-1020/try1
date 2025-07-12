stack=[]
s="0123456789ABCDEF"
top=-1
num=int(input())
base=int(input())
result=""
while True:
    top+=1
    stack.append(num%base)
    num=num//base
    if num==0:
        break
for i in range(top+1):
    result+=s[(stack.pop(top))]
    top-=1
print(result)