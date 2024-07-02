from node import Node
from linked_list import LinkedList

mylist = LinkedList()

mylist.insert_node(9)
mylist.insert_node(3)
mylist.insert_node(5)
mylist.insert_node(15)

mylist.print_list_items()
print()

print(mylist.count_nodes())
print()

print(mylist.find_node(152))
print(mylist.find_node(15))
print()

mylist.print_list_items()
mylist.delete_node(15)
mylist.print_list_items()
print()
