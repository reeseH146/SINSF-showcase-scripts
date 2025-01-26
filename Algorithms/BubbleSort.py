# Bubble sort algorithm
import random

# Bubble sort procedure
def BubbleSort(ListToSort):
    List = ListToSort[:] # Copies the list to avoid changing the original
    for x in range(len(List)-1, 1, -1): # Makes multiple passes to ensure the list is sorted
        print("\033[0;33m --- --- --- \033[0;33m")
        for y in range(x): # Loops through the list
            if List[y] > List[y+1]: # Swaps items if the current is larger than the next
                List[y], List[y+1] = List[y+1], List[y]
                print(f"\033[0;33m{List}\033[0;33m : \033[0;31m{List[y]}\033[0;31m \033[0;34m<->\033[0;34m \033[0;32m{List[y+1]}\033[0;32m")
            else:
                print(f"\033[0;33m{List}\033[0;33m : \033[0;33mNo swap\033[0;33m")
    print("\033[0;33m --- --- --- \033[0;33m")
    return List

# Main program
UnsortedList = [random.randint(0, 100) for x in range(0, 10)] # Creates an unsorted list of 25 random numbers
SortedList = BubbleSort(UnsortedList) # Sorts the list using the bubble sort algorithm
# Prints the unsorted and sorted list
print("\033[0;33mThis is a bubble sort algorithm\033[0;33m")
print(f"""\033[0;31mUnsorted list : {UnsortedList}\033[0;31m
\033[0;32mSorted list : {SortedList}\033[0;32m""")
print("""\033[0;33mA bubble sort loops through a list and moves items that are larger or equal than the next, up.
This does not always sort in 1 pass so it makes multiple passes to ensure the list is sorted.\033[0;33m""")