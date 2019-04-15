def uncompress(string):
    ret,l = '',list(string)
    for i in range(1,len(l)+1,2):
        ret += int(l[i-1])*l[i]
    return ret