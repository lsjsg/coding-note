def longest_common_prefix(string1, string2):
    string = ''
    l1,l2 = list(string1),list(string2)
    for i in range(min(len(l1),len(l2))):
        if l1[i]==l2[i]:
            string += l1[i]
        else:
            break
    return string