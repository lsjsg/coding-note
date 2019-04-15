# def createcounter():
#     def creater():
#         n=1
#         while True:
#             yield n
#             n=n+1
#     it=creater()
#     def counter():
#         return next(it)
#     return counter

def createcounter():
    a = 0
    def counter():
        nonlocal a
        a += 1
        return a
    return counter

counterA = createcounter()
print(counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createcounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

