from linked_list import LinkedList

def merge_sort(linked_list):
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head == None:
        return linked_list

    left_half, right_half = split(linked_list)