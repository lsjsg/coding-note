def f_to_c(f):
    return round((f-32)/1.8,1)

def f_to_c_approx(f):
    return round((f-30)/2,1)

def get_conversion_table_a():
    total = []
    for i in range(0,101,10):
        l = []
        l.append(i)
        l.append(f_to_c(i))
        l.append(f_to_c_approx(i))
        total.append(l)
    return total

def get_conversion_table_b():
    total = [[],[],[]]
    for f in range(0,101,10):
        total[0].append(f)
        total[1].append(f_to_c(f))
        total[2].append(f_to_c_approx(f))
    return total