# sorting algoriths
# assume contents of array are all directly comparable
from random import randint

# O(n^2)

def insertion_sort(array):
    i = 1
    while i < len(array):
        j = i
        while j > 0 and array[j] < array[j-1]:
            array[j],array[j-1] = array[j-1],array[j]
            j -= 1
        i += 1
    return array


def selection_sort(array):
    i = 0
    while i < len(array):
        j = 0
        current_max = (-1, -1)
        while j < len(array)-i:
            if current_max[0] <= array[j]:
                current_max = (array[j], j)
            j += 1
        array[len(array)-1-i],array[current_max[1]] = array[current_max[1]],array[len(array)-1-i]
        i += 1
    return array


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j and array[i] < array[j]:
                array[i],array[j] = array[j],array[i]
    return array

# O(nlogn)

def merge_sort(array):
    pass 

def quick_sort(array):
    pass 

def tree_sort(array):
    pass 

def heap_sort(array):
    pass


# conditionally < O(nlogn)

def counting_sort(array):
    pass 

def radix_sort(array):
    pass


if __name__ == '__main__':
    #print(insertion_sort([1,5,4,2]))
    #print(insertion_sort([randint(0,100) for _ in range(randint(0,100))]))
    #print(selection_sort([1,5,4,2]))
    #print(selection_sort([randint(0,100) for _ in range(randint(0,100))]))
    print(bubble_sort([1,5,4,3]))