import ast

p="""def decision(num):
    if num==1:
        return num*9
    else:
        return False
"""
t=ast.parse(p)
print(ast.dump(t))
print(t.body[0].body[0].body[0].value.n)