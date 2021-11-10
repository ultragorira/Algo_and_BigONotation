class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#O(n) time and O(n) space
def branchSums(root):
	totals = []
	sumBranches(root, 0, totals)
	return totals

def sumBranches(node, currentSum, totals):
	
	if node is None:
		return
	
	newCurrentSum = currentSum + node.value
	if node.left is None and node.right is None:
		totals.append(newCurrentSum)
		return
	
	sumBranches(node.left, newCurrentSum, totals)
	sumBranches(node.right, newCurrentSum, totals)
	