from functools import reduce
name=['asa','sdgd','ewter','rtyuruy']
Letters={'a':'A', 'b':'B', 'c':'C', 'd':'D', 'e':'E', 'f':'F', 'g':'G', 'h':'H', 'i':'I', 'j':'J', 'k':'K', 'l':'L', 'm':'M', 'n':'N', 'o':'O', 'p':'P', 'q':'Q', 'r':'R', 's':'S', 't':'T', 'u':'U', 'v':'V', 'w':'W', 'x':'X', 'y':'Y', 'z':'Z'}
l=[3, 5, 7, 9]
digits={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
def change(x):
    return str(Letters[x[0]]+x[1:])
print(list(map(change,name)))

def prod(x,y):
    return x*y
print(reduce(prod,l))

def str2float(s):
    def number(s):
        num=0
        for i in s:
            if i=='.':
                return num+1
            else:
                num+1
    def fn(x,y):
        a=0
        if a==number(s):
            a+=1
            return x 
        elif a<number(s):
            a+=1
            return 10*x+y
        else:
            a+=1
            return x+0.1*y
    def char2num(s):
        if s!='.':
            return digits[s]
    return reduce(fn,map(char2num,s))
print(str2float('23.123'))