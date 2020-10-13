class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
    
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        
        table = {}
        
        table[0] = Node(0)
        
        for child, parent in zip(pid, ppid):
            if parent not in table:
                table[parent] = Node(parent)
            
            if child not in table:
                table[child] = Node(child)
            
            table[parent].children.append(table[child])
        
        res = []
        def kill_pid(node):
            res.append(node.val)
            for child in node.children:
                kill_pid(child)
        
        kill_pid(table[kill])
        return res
            
            
