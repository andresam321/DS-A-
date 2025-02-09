from collections import deque

def level_order_traversal(root):
    if not root:
        return []
    
    queue = deque([root])  # Start with the root node
    result = []  # To store the level-order traversal
    
    while queue:
        current = queue.popleft()  # Remove the front node from the queue
        result.append(current.val)  # Process the current node
        
        # Add the left and right children of the current node to the queue
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return result
