text = """
def loop(i):
    sum=0
    for a in range(i):
        sum+=a
    return sum
"""
from Tree import *
test = Eval(text)
print(test.change_to_smaller_strings())
a=test.tree_dict()
print(a)
print(a["root"])
print(a["Module"])
