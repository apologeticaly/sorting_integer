#!python
def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Running time: The average runtime is O(n log(n)), becuase the worst situation would still not involve checking every index against all else.
    Memory usage: Since we are not creating any new data structures, the space is still O(n)"""
    # Repeat until one list is empty
    if items1 and items2:
        # Find minimum item in both lists and append it to new list
        if items1[0] > items2[0]:
            items1, items2 = items2, items1
        # Append remaining items in non-empty list to new list
        return [items1[0]] + merge(items1[1:], items2)
    return items1 + items2

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    Running time: The average runtime is O(n log(n)), as we don't have to compare each item to each other, but rather the adjacent a mirrored indeces in the other half-list.
    Memory usage: 0(n), because no new data structure is created, but rather it is being split."""

    # Check if list is so small it's already sorted (base case)
    if len(items) > 1: 
        mid = len(items) // 2

        # Split items list into approximately equal halves
        left = items[:mid]
        right = items[mid:]

        # Sort each half by recursively calling merge sort
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Merge sorted halves into one list in sorted order
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                items[k] = left[i] 
                i+= 1
            else: 
                items[k] = right[j] 
                j+= 1
            k+= 1

        while i < len(left): 
            items[k] = left[i] 
            i+= 1
            k+= 1
            
        while j < len(right): 
            items[k] = right[j] 
            j+= 1
            k+= 1
            
        return items

def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (I chose to use the last index) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    Running time: O(n log(n)) as the worst case would be checking one index against all others.
    Memory usage: O(n) as no new data is being created."""

    i = (low - 1)

    # Choose a pivot any way and document your method in docstring above
    pivot = items[high]
 
    # Loop through all items in range [low...high]
    for j in range(low, high):
        # Move items less than pivot into front of range [low...p-1]
        if items[j] <= pivot:
            i += 1
            # Move items greater than pivot into back of range [p+1...high]
            items[i], items[j] = items[j], items[i]
 
    # Move pivot item into final position [p] and return index p
    items[i+1], items[high] = items[high], items[i+1]
    return (i+1)


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    Best case running time: O(n log(n)) as there would still have to be a comparision using the pivot.
    Worst case running time: The worst case running time would be O(n^2), as there are situations where every single item has to be compared to all else.
    Memory usage: O(log(n)) as after every recursion there is a passing of the data to the next step."""


    # Check if high and low range bounds have default values (not given)
    if low == None:
        low = 0

    if high == None:
        high = len(items) - 1

    # Check if list or range is so small it's already sorted (base case)
    if len(items) == 1:
        return items

    if low < high:
        # Partition items in-place around a pivot and get index of pivot
        pi = partition(items, low, high)
 
        # Sort each sublist range by recursively calling quick sort
        quick_sort(items, low, pi-1)
        quick_sort(items, pi+1, high)