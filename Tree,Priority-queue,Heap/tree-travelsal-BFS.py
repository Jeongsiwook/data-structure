from collections import deque

def BFS(tree) :
    queue = deque()
    queue.append(tree)
    
    result = []

    while queue:
        cur = queue.popleft()
        
        if cur == None:
            continue
        
        result.append(cur.index)
        
        queue.append(cur.left)
        queue.append(cur.right)
        
    return result
