def time(h):
    multi=1
    if h!=0:
        for j in range(1,h+1):
            multi*=j
        return multi
    else:
        return 1

def C(x,y):
    c=int(time(y)/(time(x)*time(y-x)))
    return c

def triangles():
    k=0
    while(True):
        l=[]
        for i in range(k+1):
            l.append(C(i,k))
        yield l
        k=k+1

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')