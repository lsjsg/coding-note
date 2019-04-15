import ast


class Tree:
    def __init__(self,program):
        self.program=program
        self.module=ast.parse(self.program)
        self.list=[]

    def funtion_name(self):
        module = []
        arguments = []
        for node in ast.walk(self.modual):
            if isinstance(node, ast.FunctionDef):
                definition = [node, type(node).__name__, node.name]
                for i in node.args.args:
                    if i:
                        arguments[].append(i.arg)
                definition.append(arguments)
                for key in node.args:
                    if key == None or key == []:
                        pass
                    else:
                        for i in key:
                            if i:
                                arguments[].append(i.arg)
                        definition.append(arguments)


    def read(self):
        module=[]
        arguments = []
        for node in ast.walk(self.modual):
            if isinstance(node,ast.FunctionDef):
                definition = [node, type(node).__name__, node.name]

                for i in node.args.args:
                    if i:
                        arguments[].append(i.arg)
                definition.append(arguments)
                for key in node.args:
                    if key == None or key == []:
                        pass
                    else:
                        for i in key:
                            if i:
                                arguments[].append(i.arg)
                        definition.append(arguments)


    def functions(self):
        for node in ast.walk(self.module):
            if isinstance(node,ast.FunctionDef):
                return node
        pass

    def loops(self):
        pass

    def judges(self):
        pass

    def assigns(self):
        pass

    class NodeVisitor(ast.NodeVisitor):
        def __init__(self, SymbolTable):
            self.symtable = SymbolTable
            for child in SymbolTable.get_children():
                self.symtable = child
                print(child.get_symbols())

        def _visit_children(self, node):
            """Determine if the node has children and visit"""
            for _, value in ast.iter_fields(node):
                if isinstance(value, ast.FunctionDef):
                    for item in value:
                        if isinstance(item, ast.AST):
                            print(' visit item %s' % (type(item).__name__))
                            self.visit(item)
                        elif isinstance(value, ast.AST):
                            print(' visit value %s' % (type(value).__name__))
                            self.visit(value)

        def generic_visit(self, node):
            print(type(node).__name__)
            self._visit_children(node)

        def visit_Name(self, node):
            print(' variable %s type %s' % (node.id,
                                            self.symtable.lookup(node.id)))
            print(dir(self.symtable.lookup(node.id)))

    p3 = """
    def decision(num):
        if num==1:
            return True
        else:
            return False
    """
    p = ast.parse(p3)
    t = NodeVisitor(p)
    _visit_children(p)
    # print(ast.dump(ex))
    # print(ex.args[0])

    # print(ex.body)
    # print(ex.body[0].args.args[0].arg)
    # for i in ex.body[0].args.args:
    #     print(i)

    # print(type(ex.body[0]))
    # print(type(ex.body[0].args))
    # print(type(ex.body[0].args.args[0]))
    # print(type(ex.body[0].args.args[0].arg))
    # print(ex.body[0].args.args[0].arg)
    #
    # class Tree():
    #     def visit_FunctionDef(self,node):
    #         print("funcion:",node._fields)
    #
    # a=ast.parse(p3)
    # tree=Tree()
    # tree.visit_FunctionDef(a)
    from pythonds.basic.stack import Stack
    from pythonds.trees.binaryTree import BinaryTree

    def buildParseTree(fpexp):
        fplist = fpexp.split()
        pStack = Stack()
        eTree = BinaryTree('')
        pStack.push(eTree)
        currentTree = eTree
        for i in fplist:
            if i == '(':
                currentTree.insertLeft('')
                pStack.push(currentTree)
                currentTree = currentTree.getLeftChild()
            elif i not in ['+', '-', '*', '/', ')']:
                currentTree.setRootVal(int(i))
                parent = pStack.pop()
                currentTree = parent
            elif i in ['+', '-', '*', '/']:
                currentTree.setRootVal(i)
                currentTree.insertRight('')
                pStack.push(currentTree)
                currentTree = currentTree.getRightChild()
            elif i == ')':
                currentTree = pStack.pop()
            else:
                raise ValueError
            print(currentTree)
        return eTree

    pt = buildParseTree("( ( 10 + 5 ) * 3 )")
    pt.postorder()  # defined and explained in the next section