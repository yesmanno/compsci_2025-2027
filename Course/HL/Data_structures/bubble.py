# Bubble bubble bubble bubble 
# sort? what's sort? I only know bubble 
def bubbleSort(array): 
    # loop to access each array element 
    for i in range(len(array)): 
        # We will keep on track on swapping 
        swapped = False 
        # loop to compare array element 
        for j in range(0, len(array) -i-1): 
            # comparing two element 
            # change > to < to sort descending order 
            if array[j] > array[j + 1]: 

                # swap elements if 
                # elements are not in the intended order 
                temp = array[j] 
                array[j] = array[j+1] 
                array[j+1] = temp 

                swapped = True
        
        # no swapping is that array is already sorted
        # no need to go back to comapre
        if not swapped: 
            break 

arr = [-2, 45, 0, 11, -9]

print("before", arr)

bubbleSort(arr) 

print("after", arr)
