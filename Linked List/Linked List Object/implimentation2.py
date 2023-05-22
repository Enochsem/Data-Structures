from linkedlist import LinkedList


# create a linked list instantly from a list of arguments
llist = LinkedList(['a','b','c','d','e'])

print(llist)

for i in llist:
    print(i)

print(llist.insertBegining(Node(data = "f")))