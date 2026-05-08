from models import CodeFacts
import ast

def parse_code_facts(code: str):
    recursive = set()
    loops = set()
    mutating_functions = set()
    return_type = {}
    identifiers = set()
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            arg_names = {a.arg for a in node.args.args}
            mutating_methods = {
                "append",
                "extend",
                "remove",
                "pop",
                "sort",
                "reverse",
                "update",
                "clear",
                "add",
                "discard",
            }

            for child_node in ast.walk(node):
                if (
                    isinstance(child_node, ast.Call)
                    and isinstance(child_node.func, ast.Name)
                    and child_node.func.id == node.name
                ):
                    recursive.add(node.name)

                if isinstance(child_node, (ast.For, ast.While)):
                    loops.add(node.name)

                if (
                    isinstance(child_node, ast.Call)
                    and isinstance(child_node.func, ast.Attribute)
                    and isinstance(child_node.func.value, ast.Name)
                    and child_node.func.value.id in arg_names
                    and child_node.func.attr in mutating_methods
                ):
                    mutating_functions.add(node.name)

            if node.returns != None:
                return_type[node.name] = ast.unparse(node.returns)

        if isinstance(node, ast.Name):
            identifiers.add(node.id)

    return CodeFacts(recursive, loops, mutating_functions, return_type, identifiers)
