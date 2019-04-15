def get_base_counts(dna):
    a,g,c,t=0,0,0,0
    for i in list(dna):
        if i=="A":
            a+=1
        elif i=="G":
            g+=1
        elif i=="C":
            c+=1
        elif i=="T":
            t+=1
        else:
            return "The input DNA string is invalid"
    return {"A":a,"C":c,"G":g,"T":t}