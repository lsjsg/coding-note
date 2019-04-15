text = """
def loop(i):
    sum=0
    for a in range(i):
        sum+=a
    return sum
"""
from new_eval_for_ast import *
test = Eval(text)
print(test.change_to_smaller_strings())
print(test.form_new_list())