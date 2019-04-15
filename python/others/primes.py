#用filter求素数(埃氏筛法)
def odd_num():
    n=1
    while True:
        n=n+2
        yield n

def not_prime(s):
    return lambda x:x%s>0

def primes():
    yield 2
    odd=odd_num()
    while True:
        a=next(odd)
        yield a
        odd=filter(not_prime(a),odd)
for i in primes():
    if i <1000:
        print(i)
    else:
        break