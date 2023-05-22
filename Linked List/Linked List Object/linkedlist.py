from node import Node


class LinkedList():
    def __init__(self, nodes=None):
        self.head = None

        if nodes is not None: # [a,b,c,d,..]  fn = Node('a') fn.next = [index + 1]
            node = Node(data=nodes.pop(0)) #create a node object with the first element passed
            self.head = node
            for element in nodes: # create nodes and set their next element
                node.next = Node(data=element) # set the current node's next value
                # print("next ",node.next)
                node = node.next # let the previous next value be the current node
                # print(node)


    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
            # print("adding nodes to list ",node)
        nodes.append("None")
        return "->".join(nodes)

    
    def __iter__(self): # __iter__ makes the linked list iterable
        node = self.head
        while node is not None:
            yield node
            node = node.next

    
    def insertBegining(self,node):
        node.next = self.head  # set the head as the new nodes next reference to create a connection
        self.head = node 


    def insertEnd(self, node):
        if self.head == None: # if there are no nodes set the node as head
            self.head = node
            return
        for currentNode in self: # loop till last node and set lastnode.next to new node
            pass
        currentNode.next = node


    def insertAfter(self, targetNode, newNode):
        if self.head is None:
            raise Exception("Linked List Object is empty")
        for node in self:
            if node.data == targetNode:
                newNode.next = node.next # set the old next value pointer to the new node next to maintain the link
                node.next = newNode  # then now connect the old node next to the new node it self
                return
        raise Exception(f'Node with data "{targetNode}" not FOUND!!')

    
    def insertBefore (self, targetNodeData, newNode):
        if self.head is None:
            raise Exception("Linked List Object is empty")

        if self.head.data == targetNodeData:
            return self.insertBegining(newNode)

        previousNode = self.head  # start at the head and set the head to the initial privous node
        for node in self:
            if targetNodeData == node.data:
                previousNode.next = newNode # set the previous node next to the new node
                newNode.next = node  # and the new node next to the current node
                return
            previousNode = node # set the current node as the previous node
        raise Exception(f'Node with data "{targetNode}" not FOUND!!')


    def removeNode (self, targetNodeData):
        if self.head is None:
            raise Exception("Linked List Object is empty")

        if self.head.data == targetNodeData: # if there is only one node in the linked list
            self.head = self.head.next # set the head data to None
            return
        
        previousNode = self.head
        for node in self:
            if targetNodeData == node.data:
                previousNode.next = node.next # set the target node next to the previous node next
                return
            previousNode = node

        raise Exception(f'Node with data "{targetNode}" not FOUND!!')

    
    def getIndex(self,index):
        data = ""
        if self.head is None:
            raise Exception("Linked List Object is empty")
        count = 0
        for node in self:
            if count == index:
                data = node.data
                print(data)
            count += 1
        return data
        # raise Exception(f'Index {index} is out of range') 