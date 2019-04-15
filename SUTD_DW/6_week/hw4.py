def get_fundamental_constants(f):
    lines = f.readlines()
    ret = {}
    for cons in lines[2:]:
        name,value,_ = cons.strip().split()
        ret[name] = float(value)
    return ret