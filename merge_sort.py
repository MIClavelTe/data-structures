def merge_sort (list):
    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split (list):
    mid = len(list)//2
    lef = list[:mid]
    right = list[mid:]

    return left,right
