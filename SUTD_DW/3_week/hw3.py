def is_prime(n):
    if n<2:
        return False
    elif n==2:
        return True
    else:
        for i in range(2,int(n/2)):
            if n%i==0:
                return False
        return True
            