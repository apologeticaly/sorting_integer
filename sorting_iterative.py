def is_sorted(input):
    for i in range(len(input) - 1):
        if input[i] <= input[i + 1]:
            pass
        else:
            return False
    return True

def bubble_sort (input):
    for i in range(len(input)):
        for j in range(len(input) - 1):
            if input[j] > input[j+1]:
                input[j], input[j+1] = input[j+1], input[j]
    return (input)

def selection_sort(input):
    for i in range(len(input) - 1):
        min = i
        for j in range(len(input) - 1):
            if input[min] <= input[j]:
                input[min], input[j] = input[j], input[min]
    return input

def insertion_sort(input): 
    for i in range(len(input) - 1): 
        min = input[i] 
        j = i-1
        while j >=0 and min < input[j] : 
                input[j+1] = input[j] 
                j -= 1
        input[j+1] = min
    return input