from collections import deque

#print(type(deque()))

# creating a linked list
deque()

# a linked list with values
deque([9,8,3])
deque(["9","8","3"])
deque([{'data':'a'}, {'data':'b'}])

llist = deque('abcdef')
llist.append('x')
print(llist)
llist.pop()
print(llist)

llist.appendleft("x")
print(llist)
llist.popleft()
print(llist)