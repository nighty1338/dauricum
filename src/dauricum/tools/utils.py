import random, ast

class Utils:
    def randomize_name(alphabet: str, length: int) -> str:
        name = ''.join([random.choice(alphabet) for _ in range(length)])
        while name[0].isdigit():
            name = ''.join([random.choice(alphabet) for _ in range(length)])
        
        # name = name[:len(name) // 2] + '__dauricum__' + name[len(name) // 2:] watermark
        
        return name
    def generate_next_num(current: int, max: int):
        next = current + random.randint(1, 1000)
        
        if next > max:
            raise EOFError('BAD CONTROL FLOW BLOCK NUMBER (report this issue on github)')
        return next
    def find_parent(node, targets):
        parent = node.parent
        
        while True:
            for target in targets:
                if isinstance(parent, target):
                    return parent
                elif isinstance(parent, ast.Module):
                    return None
            parent = parent.parent
    def find_class(tree, node: ast.Call):
        for _node in ast.walk(tree):
            for child in ast.iter_child_nodes(_node):
                name = node.func.id
                if isinstance(child, ast.FunctionDef):
                    
                    if child.name == name:
                        return child.parent
                elif isinstance(child, ast.ClassDef):
                    
                    if child.name == name:
                        return child
        return None
    def get_chance():
        return random.randint(0, 100)
