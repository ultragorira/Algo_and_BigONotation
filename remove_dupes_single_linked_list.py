class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
	
	currentNode = linkedList
	while currentNode is not None: #Else we are at the tail of the linkedlist
		nextNode = currentNode.next #Check to what this node is pointing to
		while nextNode is not None and nextNode.value == currentNode.value: #Check all node that are same until different found
			nextNode = nextNode.next
		
		currentNode.next = nextNode
		currentNode = nextNode
	
	return linkedList
	