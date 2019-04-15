import ast

class Tree(ast.NodeVisitor):

    # def generic_visit(self, node):
    #     print(type(node).__name__)
    #     ast.NodeVisitor.generic_visit(self,node)
    #
    # def visit_FunctionDef(self,node):
    #     print(type(node).__name__)
    #     ast.NodeVisitor.generic_visit(self,node)
    #
    # def visite_Assign(self,node):
    #     print(type(node).__name__)
    #     ast.NodeVisitor.generic_visit(self,node)
    def function(self):
        if isinstance(node,ast.FunctionDef):
            print("function definition:",node.name)

    def assign(self):
        if isinstance(node.ast.Module):
            print("import module:",node.name)

    def (self):
        if isinstance(node,ast.While):
            print("while statement:")
