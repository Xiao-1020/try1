def can_colour(colour,code):
    for i in familar[code]:
        if colours[i]==colour:
            return False
    return True

def dye(colour_num,current,colours):
    for i in range(1,colour_num+1):
        if can_colour(i,current):
            colours[current]=i
            if current==n:
                return True
            if dye(colour_num,current+1,colours):
                return True
            colours[current]=0
    return False

def outcome(n):
    for i in range(1,n):
        if dye(i,1,colours):
            return i
    return n

n=int(input())
m=int(input())
familar={}
colours=[0 for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    if a in familar:
        familar[a].append(b)
    else:
        familar[a]=[b]
    if b in familar:
        familar[b].append(a)
    else:
        familar[b]=[a]
print(outcome(n))