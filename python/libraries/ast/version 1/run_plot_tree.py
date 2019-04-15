import ast
from plot_tree import *


p1="""
say="hello world"
print(say)
"""
p2="""
def gravity(weight):
    g=9.8
    return 9.8*weight
"""
p3="""
def decision(num):
    if num==1:
        return True
    else:
        return False
"""
p4="""
def loop(i):
    sum=0
    for a in range(i):
        sum+=a
    return sum
"""

t1=Tree(p1)
t1.plot()
t2=Tree(p2)
t2.plot()
t3=Tree(p3)
t3.plot()
t4=Tree(p4)
t4.plot()
a = ast.parse(p1)
a.damp()