def binary_to_decimal(binstr):
    num,ret = list(binstr),0
    for i in range(len(num)):
        ret += 2**i * int(num[-i-1])
    return ret
    