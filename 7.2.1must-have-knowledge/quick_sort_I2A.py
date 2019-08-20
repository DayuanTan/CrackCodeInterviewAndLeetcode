# quick sort (in place) following the alg from Introduction to Algorithm
# Running time: avg O(nlogn), worst O(n^2), best O(logn)

import random

# init
#rand_array=[int(random.random()*100)]
rand_array=[]
#rand_array=[9, 8, 7, 6, 5, 4, 3, 2, 1]
for i in range(1,11):
    rand_array.append(random.randrange(1,1000))

print("Initial random array is:", rand_array)

def swap(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]

# partition
def partition(array, left_index, right_index):
    pivot_value = array[right_index] # always use the right most as pivot

    i = left_index - 1 
    for j in range(left_index, right_index):
        if array[j] <= pivot_value:
            i = i + 1
            swap(array, i, j)
    swap(array, i+1, right_index)
    return i+1


# quick sort 
def quicksort(init_array, left=0, right=None):
    if right == None:
        right = len(init_array) - 1
    if left < right:
        mid_index = partition(init_array, left, right)
        quicksort(init_array, left, mid_index - 1)
        quicksort(init_array, mid_index + 1, right)

    
        


# main
quicksort(rand_array)
print("Sorted array:", rand_array)