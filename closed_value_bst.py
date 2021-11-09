def findClosestValueInBst(tree, target):
	return find_closest_value_bst(tree, target, tree.value)

#Average O(log(N)) time, O(log(N)) space
#Worst case O(N) time, O(log(n)) Space

def find_closest_value_bst(tree, target, closest_value):
	if tree is None:
		return closest_value
	if abs(target - closest_value) > abs(target - tree.value):
		closest_value = tree.value
	if target < tree.value:
		return find_closest_value_bst(tree.left, target, closest_value)
	elif target > tree.value:
		return find_closest_value_bst(tree.right, target, closest_value)
	else:
		return closest_value
	
#Average O(log(N)) time, O(1) space
#Worst case O(N) time => If tree with single branches, O(1) Space    
def find_closest_value_bst_iterate(tree, target, closest_value):
	
    current_node = tree
    while current_node is not None:
        if abs(target - closest_value) > abs(target - current_node.value):
            closest_value = current_node.value
        if target < current_node.value:
            return find_closest_value_bst(current_node.left, target, closest_value)
        elif target > current_node.value:
            return find_closest_value_bst(current_node.right, target, closest_value)
        else:
            break

    return closest_value

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

