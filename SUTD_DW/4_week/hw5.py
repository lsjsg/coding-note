def diff(p):
    dp = {}
    for k in p.keys():
        if k <= 0:
            pass
        else:        
            dp[k-1] = k*p[k]
    return dp