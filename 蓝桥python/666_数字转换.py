def converse(n):
    if n=='0':
        return '0'
    return str(int(str(int(n))[::-1]))

def in_converse(n):
    if '.' in n:
        a,b=n.split('.')
        return converse(a)+'.'+converse(b)
    if '/'in n:
        a,b=n.split('/')
        return converse(a)+'/'+converse(b)
    if n[-1]=='%':
        return converse(n[:-1])+'%'
    else:
        return converse(n)

print(in_converse(input()))