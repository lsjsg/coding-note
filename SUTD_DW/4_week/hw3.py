def multiplication_table(n):
    if n<1:
        return None
    else:
        l=[]
        for i in range(1,n+1):
            l.append(list(map(lambda x:x*i,list(range(1,n+1)))))
        return l
            