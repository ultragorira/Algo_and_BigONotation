#O(n) time and O(h) space (height of the tree)
#Recuservely.

def nodeDepths(root, depth=0):
	if root is None:
		return 0
	return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)

#Iteratively, O(n) time and O(h) space (height of the tree)

def nodeDepths(root):
    sum_depths = 0
    stack = [{"node": root, "depth": 0}]
    while len(stack) > 0:
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]
        if node is None:
            continue
        sum_depths += depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})
    
    return sum_depths



class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
