def find_average(lst):
    suml, a, num=0.0,[],0
    for l in lst:
        if l==[]:
            a.append(0.0)
        else:
            a.append(sum(l)/len(l))
            suml+=sum(l)
            num += len(l)
    return a,suml/num