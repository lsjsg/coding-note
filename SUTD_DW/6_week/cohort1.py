def reverse(string):
    l,ret = list(string),''
    for i in range(len(l)):
        ret += l[-i-1]
    return ret
    