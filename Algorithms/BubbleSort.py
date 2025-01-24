# Bubble sort algorithm
import random

# Bubble sort procedure
def BubbleSort(ListToSort):
    List = ListToSort
    for x in range(len(List)-1): # Makes multiple passes to ensure the list is sorted
        for y in range(x): # Loops through the list
            if List[y] > List[y+1]: # Swaps items if the current is larger than the next
                List[y], List[y+1] = List[y+1], List[y]
    return List

# Main program
UnsortedList = [random.randint(0, 100) for x in range(0, 25)] # Creates an unsorted list of 25 random numbers
SortedList = BubbleSort(UnsortedList) # Sorts the list using the bubble sort algorithm
# Prints the unsorted and sorted list
print("\033[0;33mThis is a bubble sort algorithm\033[0;33m")
print(f"""\033[0;31mUnsorted list : {UnsortedList}\033[0;31m
\033[0;32mSorted list : {SortedList}\033[0;32m""")
print("""\033[0;33mA bubble sort loops through a list and moves items that are larger or equal than the next, up.
This does not always sort in 1 pass so it makes multiple passes to ensure the list is sorted.\033[0;33m""")