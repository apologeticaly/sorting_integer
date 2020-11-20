#!python
import random
from sorting_iterative import insertion_sort

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: O(n+k) because each index only needs to be gone over once, with the max amount of counts being the maximum value in the list (k).
    Memory usage: O(k) because in the best case scenario there is no need to create a new list."""    
    
    # FIXME: Improve this to mutate input instead of creating new output list
    
    if len(numbers) < 1:
        return

    output = []
    count = []
    
    # Find range of given numbers (minimum and maximum integer values)
    maximum = max(numbers)

    # Create list of counts with a slot for each number in input range
    for item in range(len(numbers)):
        output.append(0)

    for item in range(0, maximum + 1):
        count.append(0)

    # Loop over given numbers and increment each number's count
    for item in range(len(numbers)):
        count[numbers[item]] += 1
    
    for i in range(1, len(count)):
        count[i] = count[i] + count[i-1]

    # Loop over counts and append that many numbers into output list
    for i in range(len(numbers)):
        output[count[numbers[i]]-1] = numbers[i] 
        count[numbers[i]] -= 1

    return output



def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    Running time: O(n+k) because each index only needs to be gone over once, with the max amount of counts being the maximum value in the list (k). Worst case would be O(n^2) where every item in every bucket must be sorted.
    TODO: Memory usage: O(n), because no new data structure needs to be created."""
    
    # FIXME: Improve this to mutate input instead of creating new output list

    if len(numbers) < 1:
        return

    # Find range of given numbers (minimum and maximum values)  
    key = max(numbers) / len(numbers)
    
    # Create list of buckets to store numbers in subranges of input range
    buckets = []

    for i in range(len(numbers)):
        buckets.append([])

    # Loop over given numbers and place each item in appropriate bucket
    for i in range(len(numbers)):
        j = int(numbers[i] / key)
        if j != len(numbers):
            buckets[j].append(numbers[i])
        else:
            buckets[len(numbers) - 1].append(numbers[i])
 
    # Sort each bucket using any sorting algorithm (recursive or another)
    for i in range(len(numbers)):
        insertion_sort(buckets[i])
 
    output = []

    # Loop over buckets and append each bucket's numbers into output list
    for i in range(len(numbers)):
        output = output + buckets[i]
 
    return output

print('counting_sort ' + str(counting_sort([13, 3, 16, 13, 10, 16, 12, 14, 13, 7, 5])))
print('bucket_sort   ' + str(bucket_sort([13, 3, 16, 13, 10, 16, 12, 14, 13, 7, 5])))