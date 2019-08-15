# quick sort (divide and conquer)
# Running time: avg O(nlogn), worst O(n^2)

import random

# init
rand_array=[int(random.random()*100)]
for i in range(1,10):
    rand_array.append(random.randrange(1,1000))

print("Initial random array is:", rand_array)

# concatenate 2 arrays and 1 int into one array
def concatenate(array1, pivot, array3):    
    array1.append(pivot)
    if len(array3) > 0:
        for i in range(len(array3)):
            array1.append(array3[i])     
    return array1

# quick sort divide and conquer 
def quicksort(init_array):
    leng = len(init_array)

    if leng >= 2:
        pivotIndex = random.randrange(1, leng)
        pivotValue = init_array[pivotIndex] 

        # cut array into 3 parts
        less = []
        greater = []
        for i in range(0, leng):
            if init_array[i] < pivotValue:
                less.append(init_array[i])
            elif init_array[i] > pivotValue:
                greater.append(init_array[i])

        return concatenate(quicksort(less), pivotValue, quicksort(greater))
    else:
        return init_array


# main
sortedarray = quicksort(rand_array)
print("Sorted array:", sortedarray)