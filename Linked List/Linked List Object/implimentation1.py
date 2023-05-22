from linkedlist import LinkedList
from node import Node


#create a linked list
llist = LinkedList()
# print(type(llist))

# creating a node
node1 = Node("a")


# adding a node to the linked list 
llist.head = node1
print(llist)
# print(llist.__str__())


node2 = Node("b")
node3 = Node('c')
node1.next = node2
node2.next = node3

print(llist)
# print(node3.__dict__)