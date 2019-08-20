# quick sort (in place)
# Running time: avg O(nlogn), worst O(n^2), best O(logn)

import random

# init
rand_array=[int(random.random()*100)]
#rand_array=[9, 8, 7, 6, 5, 4, 3, 2, 1]
for i in range(1,10):
    rand_array.append(random.randrange(1,1000))

print("Initial random array is:", rand_array)

def swap(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]

# partition
def partition(array, left_index, right_index, pivot_value):

    while(left_index < right_index):
        while(array[left_index] < pivot_value):
            left_index += 1
            #print("left -:", left_index)
        while( (array[right_index] > pivot_value) and right_index > 0):
            right_index -= 1
            #print("right -:",right_index)
        if left_index < right_index:
            swap(array, left_index, right_index)
    #print("return left index:", left_index)
    return left_index


# quick sort 
def quicksort(init_array, left=0, right=None):
    if right == None:
        right = len(init_array) - 1
    if left < right - 1:
        pivot_value = init_array[left + ((right - left) // 2)]
        mid_index = partition(init_array, left, right, pivot_value)
        #print("input left mid_index right:", left, mid_index, right)
        quicksort(init_array, left, mid_index - 1)
        quicksort(init_array, mid_index, right)

    
        


# main
quicksort(rand_array)
print("Sorted array:", rand_array)