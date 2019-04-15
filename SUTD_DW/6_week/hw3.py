def get_base_counts2(dna):
    ret = {"A":0,"G":0,"C":0,"T":0}
    for i in list(dna):
        if not (i.isupper()):
            return 'The input DNA string is invalid'
        elif i in ret.keys():
            ret[i]+=1
    return ret