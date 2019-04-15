import ast


class CodeVisitor(ast.NodeVisitor):
    def generic_visit(self, node):
        print(type(node).__name__)
        ast.NodeVisitor.generic_visit(self, node)

    # def visit_FunctionDef(self, node):
    #     print(type(node).__name__)
    #     ast.NodeVisitor.generic_visit(self, node)
    #
    # def visit_Assign(self, node):
    #     print(type(node).__name__)
    #     ast.NodeVisitor.generic_visit(self, node)
    #
if __name__ == "__main__":
    code = open("test.py","r")
    ex=""
    for lines in code.readlines():
        ex+=lines
    tree = CodeVisitor()
    tree.generic_visit(ex)