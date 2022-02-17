#O(n) space and time
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def validateBst(tree):
	return min_max(tree, float("-inf"), float("inf"))

def min_max(tree, min_value, max_value):		
	if tree is None: #We are at the bottom, leaf
		return True
	if tree.value < min_value or tree.value >= max_value:
		return False
	left_is_valid = min_max(tree.left, min_value, tree.value) #recursive call passing left 
	return left_is_valid and min_max(tree.right, tree.value, max_value)
	
