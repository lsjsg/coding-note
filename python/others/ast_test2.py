import ast

program=r"""
def hello_world():
    say="hello world"
    print(say)
hello_world()
"""

tree=ast.parse(program)

