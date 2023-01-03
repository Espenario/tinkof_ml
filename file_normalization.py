import ast
import numpy as np

class FileOptimizer(ast.NodeTransformer):

    def __init__(self):
        self._arg_count = 0
        self.var_dict = {}
        self._var_count = 0

    def visit_arg(self, node):
        node.arg = "arg_{}".format(self._arg_count)
        self._arg_count += 1
        self.generic_visit(node)
        return node

    def visit_Name(self, node):
        if node.id not in self.var_dict:
            self.var_dict[node.id] = "var_{}".format(self._var_count)
        node.id = self.var_dict[node.id]
        self._var_count += 1
        self.generic_visit(node)
        return node

    def visit_Module(self, node: ast.Module):
        ast.get_docstring(node, clean=False)
        self.generic_visit(node)
        return node

    def visit_FunctionDef(self, node: ast.FunctionDef):
        ast.get_docstring(node, clean=True)
        self.generic_visit(node)
        return node

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        ast.get_docstring(node, clean=True)
        self.generic_visit(node)
        return node

    def visit_ClassDef(self, node: ast.ClassDef):
        ast.get_docstring(node, clean=True)
        self.generic_visit(node)
        return node
    