def most_frequent(lst):
    fre = {}
    l={}
    for i in lst:
        if i in fre:
            fre[i]+=1
        else:
            fre[i]=1
    ans = []
    for k,a in fre.items():
        if a == max(fre.values()):
            ans.append(k)
    return ans