import ast

code = open("test.py", "r")
ex = ""
for lines in code.readlines():
    ex += lines
tree=ast.parse(ex)
for node in ast.walk(tree):
    #if isinstance(node, ast.FunctionDef):
    print(node)