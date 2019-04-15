import ast

def tree(file):
    code = ""
    result = []
    res = open(file,"r",encoding = "UTF-8")
    for line in res.readlines():
        code += line
    ex = ast.parse(code,filename=file,mode="exec")
    result += [ast.dump(ex)]
    return result
print(tree("test.py")[0])
# testline = tree("test.py")[0]
# testline3 = eval(testline)
# testline2 = testline.split(",")
# for node in testline2:
#     print(node)

# general_tree = tree("test.py")
# for node in general_tree:
#     for nodes in node:
# #        print(nodes)
#         pass
