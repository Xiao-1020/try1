def listsum(lst):
    if len(lst)==1:
        return(lst[0])
    else:
        return(lst[0]+listsum(lst[1:]))


lst=eval(input())
print(listsum(lst))