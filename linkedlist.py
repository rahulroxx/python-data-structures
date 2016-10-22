class Node(object):

    def __init__(self, data, next=None):

        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)



class LinkedList(object):



    def __init__(self):

        self.head = None
        self.size = 0


    def add_elem(self, data):
            if not self.head:
                n = Node(data)
                self.head = n
                return
            else:
                n = self.head

                while n.next != None:
                    n = n.next

                new_node = Node(data)
                n.next = new_node;
                return


    def isEmpty(self):
        return not self.head

    def add_list(self, list_temp):
        n = self.head
        while n.next != None:
            n = n.next
        n.next = list_temp.head

    def printList(self):
        n = self.head

        while n:
            print str(n)
            n = n.next

ll = LinkedList()
l2 = LinkedList()
elems = [1, 2, 3, 54, 6]
elems1 = [33,65,31,5]
for elem in elems:
    ll.add_elem(elem)
for elem in elems1:
    l2.add_elem(elem)

ll.add_list(l2)
ll.printList()
