def coverse(origin,base):
    s="0123456789ABCDEF"
    if origin<base:
        return(origin)
    else:
        return(str(coverse(origin//base,base))+s[origin%base])

origin=int(input())
base=int(input())
print(coverse(origin,base))