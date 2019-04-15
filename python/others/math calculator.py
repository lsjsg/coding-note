from math import sqrt
A=input("the first point:")
B=input("the second point:")
C=input("the third point:")
print(A,B,C)
def vector(x,y):
    l=[]
    for i in range(3):
        s,t=x[i],y[i]
        p=int(s)-int(t)
        l.append(p)
    return l
def length(x):
    sum=0
    for i in range(3):
        sum+=x[i]**2
    return sum**0.5
def dotproduct(x,y):
    sum=0
    for i in range(3):
        sum+=x[i]*y[i]
    return sum
a=vector(A,B)
b=vector(A,C)
c=vector(B,C)
cos=dotproduct(a,b)/(length(a)*length(b))
sin=(1-cos**2)**0.5
area=length(a)*length(b)*sin*0.5
print(area)
