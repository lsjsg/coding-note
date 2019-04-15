def compound_value_months(amt, rate, months):
    sum,n ,rate = 0, 0, rate/12
    while n<months:
        sum=(sum + amt)*(rate + 1)
        n+=1
    return round(sum,2)
        