# TO-DO: Complete the selection_sort() function below
'''
repeat (numOfElements - 1) times

  set the first unsorted element as the minimum

  for each of the unsorted elements

    if element < currentMinimum

      set element as new minimum

  swap minimum with first unsorted position
  '''

def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j


        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
'''do

  swapped = false

  for i = 1 to indexOfLastUnsortedElement-1

    if leftElement > rightElement

      swap(leftElement, rightElement)

      swapped = true; swapCounter++

while swapped'''

def bubble_sort(arr):
    swap_made = True
    while swap_made == True:
        swap_made = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap_made = True


    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
# O(n+k) : Time
# O(n + k) : Space

'''
create key (counting) array

for each element in list

  increase the respective counter by 1

for each counter, starting from smallest key

  while counter is non-zero

    restore element to list

    decrease counter by 1
    '''

# def counting_sort(arr, maximum=None):
#     count_arr = [0 for i in range(maximum)]
#     count = [0 for i in range(maximum)]

#     ans = ["" for _ in arr]

#     for i in arr:
#         count[ord(i)] += 1

#     for i in range(maximum):
#         count[i] += count[i-1]

#     for i in range(len(arr)):
#         count_arr[count[ord(arr[i])] -1] = arr[i]
#         count[ord(arr[i])] -= 1

#     for i in range(len(arr)):
#         ans[i] = count_arr[i]
#         count_arr[i] = arr[i]

#     return arr

# def counting_sort(arr, maximum):
#     m = maximum + 1
#     count = [0] * m

#     for n in arr:
#         count[n] += 1
    
#     i = 0

#     for n in range(m):
#         for c in range(count[n]):
#             arr[i] = n
#             i += 1
#     return arr


def counting_sort(arr, maximum = -1):
    # check for empty array
    if len(arr) == 0:
        return arr

    max = arr[0] # find largest element in array

    for num in arr:
        if num < 0:
            # raise Exception("Error, negative numbers not allowed in Count Sort")
            return("Error, negative numbers not allowed in Count Sort")
        if num > max:
            max = num 
    
    # Count the number of times each value appears.
    # counts[0] stores the number of 0's in the input
    # counts[4] stores the number of 4's in the input

    counts = [0] * (max + 1)
    for num in arr:
        counts[num] += 1

    # Overwrite counts to hold the next index an num with
    # a given value goes. So, counts[4] will now store the index
    # where the next 4 goes, not the number of 4's our
    # list has.
    num_items_before = 0
    for i, count in enumerate(counts):
        counts[i] = num_items_before
        num_items_before += count

    # Output list to be filled in
    sorted_list = [None] * len(arr)

    # Run through the input list
    for num in arr:
        
        # Place the num in the sorted list
        sorted_list[ counts[num] ] = num

        # And, make sure the next num we see with the same value
        # goes after the one we just placed
        counts[num] += 1

    return sorted_list
