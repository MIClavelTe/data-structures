# data-structures

Access - numbers[0]  |  Search - numbers.index(0)  |  Length - len(list)

Append - list.append(1)  |  Extend - list.extend([2,3,4])  |  Insert - list.insert(5,6)

Remove - list.remove(6)

# linked_list.py

Create a Node structure with data and a reference to the next node

Create a Linked List structure with is_empty, size, add, search, insert, and remove methods

is_empty returns true or false if there is a head node

size adds 1 to a counter until current reaches the tail node then returns the count

add takes a parameter of data and creates a new head node with the data

search takes a parameter of key and returns the value of current if it's equal to the key or returns none if the key is not found.

insert takes a parameter of data for the new node and an index of where to place the node. If the index is equal to 0, it uses the add method. If not, it uses a while loop until current is in the index and places the new node between current and current.next_node

remove takes a parameter of key for what to remove. A while checks 3 outcomes. If current is head and it's value is equal to the key, the new head is now current.next_node. If current is not head but it's value is equal to the key, previous.next_node would equal current.next_node. Else, the previous node would be current and current would be current.next_node.
