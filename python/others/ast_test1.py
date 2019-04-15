import ast

program1=r"""
def hello_world():
    say="hello world"
    print(say)
hello_world()
"""

program2=r"""
def loop():
    for i in range(4):
        print(i)
loop()
"""

program3=r"""
num=1
def if_condition():
    if num==1:
        print(True)
"""

program4="""
i=0
def while_condition():
    while i<5:
        i+=1
    print(i)
"""

tree1=ast.parse(program1)
tree2=ast.parse(program2)
tree3=ast.parse(program3)
tree4=ast.parse(program4)
ast.compile(program1)