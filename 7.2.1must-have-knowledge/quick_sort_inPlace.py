# quick sort (in place)
# Running time: avg O(nlogn), worst O(n^2), best O(logn)

import random

# init
rand_array=[int(random.random()*100)]
for i in range(1,10):
    rand_array.append(random.randrange(1,1000))

print("Initial random array is:", rand_array)

def swap(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]
    return array

# partition
def partition(array, left_index, right_index, pivot_value):

    print("a:",array)
    print("p:",pivot_value)
    print("left:", left_index)
    print("r:",right_index)
    while(left_index < right_index):
        while(array[left_index] < pivot_value):
            left_index += 1
            print("left-:", left_index)
        while(array[right_index] > pivot_value):
            right_index -= 1
            print("r-:",right_index)
        if left_index < right_index:
            swap(array, left_index, right_index)
    return left_index


# quick sort divide and conquer 
def quicksort(init_array, left=0, right=None):
    if right == None:
        right = len(init_array) - 1
    print("q l:",left)
    print("q r:",right)
    if left < right:
        pivot_value = init_array[(right - left) // 2]
        print("q p:",pivot_value)
        mid_index = partition(init_array, left, right, pivot_value)
        quicksort(init_array, left, mid_index - 1)
        quicksort(init_array, mid_index, right)

    
        


# main
quicksort(rand_array)
print("Sorted array:", rand_array)