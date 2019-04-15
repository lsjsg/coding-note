import ast


class Tree():
    def __init__(self,program):
        self.program=ast.parse(program)
        self.tree=[]


    def AugAssign_tree(self,node):
        AugAssign={}
        AugAssign["target name"]=node.target.id
        AugAssign["value name"]=node.value.id
        AugAssign["operation"]=node.op
        return AugAssign


    def Assign_tree(self,node):
        Assign={}
        Assign["target name"]=node.targets
        Assign["value"]=node.value
        return Assign


    def Expr_tree(self,node):
        Expr={}
        Expr["Func name"]=node.value.func.id
        Expr["value"]=node.value.args
        return Expr


    def while_tree(self,node):
        While={}
        While["left"]=node.test.left.id
        While["operation"]=node.test.ops
        While["right"]=node.test.comparators.n
        While["body"] = self.test(node.body)
        return While


    def for_tree(self,node):
        For={}
        For["arg name"]=node.target.id
        For["range"]=node.iter
        For["body"]=self.test(node.body)
        return For


    def if_tree(self,node):
        If={}
        print('node:',node)
        if node.test:
            If["left"]=node.test.left.id
            If["operation"]=node.test.ops
            If["comparator"]=node.test.comparators
            if isinstance(node.body,ast.Return):
                If["returns"].append(self.Return_tree(node.body))
            else:
                If["body"]=self.test(node.body)
            if node.orelse:
                for i in node.orelse:
                    If["or else"]=self.orelse_tree(i)
        return If


    def orelse_tree(self,node):
        return self.if_tree(node)


    def function_tree(self,node):
        Function = {}
        Function["name"] = node.name
        if node.args:
            args = {}
            for i in node.args.args:
                print(i)
                print(i.arg)
                args["args"] = i.arg
                if i.annotation:
                    args["annotation"] = i.annotation
            Function["args"] = args
        Function["returns"]=[]
        if isinstance(node.body,ast.Return):
            Function["returns"].append(self.Return_tree(node.body))
        else:
            Function["body"]=self.test(node.body)
        return Function


    def Return_tree(self,node):
        Return={}
        if node.value.left and node.value.right:
            Return["value"] = [node.value.left,node.value.right]
        elif node.value.value:
            Return["value"] = node.value.value
        elif node.value.id:
            Return["value"] = node.value.id
        elif node.value.value.n:
            Return["value"] = node.value.n


    def test(self,node):
        body=[]
        for parts in node:
            if isinstance(parts,ast.FunctionDef):
                body.append(self.function_tree(parts))

            if isinstance(parts, ast.If):
                body.append(self.if_tree(parts))

            elif isinstance(parts, ast.While):
                body.append(self.while_tree(parts))

            elif isinstance(parts, ast.For):
                body.append(self.for_tree(parts))

            elif isinstance(parts, ast.Expr):
                body.append(self.Expr_tree(parts))

            elif isinstance(parts, ast.Assign):
                body.append(self.Assign_tree(parts))

            elif isinstance(parts, ast.AugAssign):
                body.append(self.AugAssign_tree(parts))

            elif isinstance(parts,ast.Return):
                body.append(self.Return_tree(parts))
        return body


    def plot(self):
        self.tree=self.test(self.program.body)
        print(self.tree)