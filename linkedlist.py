class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next


class LinkedList:
	def __init__(self, head=None):
		self.head = head

	def add_item(self, data):
		if self.head is None:
			n = Node(data)
			self.head = n
		else:
			temp = self.head
			while temp.next != None:
				temp = temp.next
			n = Node(data)
			temp.next = n

	def printList(self):
		n = self.head 
		while n:
			print n.data
			n = n.next 

ll = LinkedList()
elems = [1, 2, 3, 54, 6]
print elems
for elem in elems:
    ll.add_item(elem)

ll.printList()