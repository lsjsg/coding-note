# NB: you do not need to submit the 'get_data' function

def extract_values(values):
    l = values.split()
    return int(l[0]),int(l[1])         

def calc_ratios(values):
    if values[1]!=0:
        return values[0]/values[1]