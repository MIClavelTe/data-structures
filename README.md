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

# merge_sort.py

Create a top level merge_sort method that uses 2 other methods, split and merge

merge_sort sorts a list in acscending order and returns a new list. It uses divide, conquer, and combine. Divide finds the midpoint the list then divides into sublists. Conquer recursively sorts the sublists. Combine merges the sublists created into a sorted list.

The base case of merge_sort is that it returns the list if the list is empty or is a single element list. merge_sort splits the list by the midpoint then recursively splits those halves over and over until there are only single element sublists. Then the sublists merge together backwards in order until they become a new sorted list.

merge_sort uses the method split that takes a parameter of a list. Split divides then floors the length of the list by 2. It creates a left list that starts from the beginning of the list till the midpoint and a right list that starts from the midpoint till the end. Split returns the 2 lists, left and right.

merge_sort uses the merge method. It takes 2 parameters. A left list and a right list. It creates an empty list and 2 variables, i and j. i for the left list and j for the right. There are 3 while loops. While i is less than the length of the left list and j is less than the length of the right list, it goes through a condition. If left[i] is less than right[j], the new list appends left[i] and i is added 1. Else, the new list appends right[j] and j is added 1. While i is less than the length of the left list, the new list appends left[i] and adds 1 to i. The next while loop is the same except it goes for j and the right list. Lastly, merge mthod returns the new list with all the sorted values.

verify_sorted takes a parameter of list. It checks if the list has been sorted or not. If the length of the given list equals 0 or 1, it returns True, the list has been sorted. If not, verify_sorted returns true or false if list[0] is less than list[1] and recursively calls itself until it checks if the  dlist is in order.
