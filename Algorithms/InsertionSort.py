# Insertion sort
import random

# Insertion sort
def InsertionSort(ListToSort):
    List = ListToSort[:] # Copies the list to avoid changing the original
    for x in range(1, len(List)): # Loops through the list
        print("\033[0;33m --- --- --- \033[0;33m")
        if List[x] < List[x - 1]: # Checks if the current item is smaller than the previous
            CurrentItem = List[x]
            PreviousItem = List[x - 1]
            print(f"\033[0;33m{List}\033[0;33m : \033[0;31m {PreviousItem} > {CurrentItem}\033[0;31m")
            for y in range(x, 0, -1): # Loops back through the list until the item is sorted
                if List[y] < List[y - 1]: # Swaps the items if the current is smaller than the previous
                    List[y - 1], List[y] = List[y], List[y - 1] # Swaps the items
                    print(f"\033[0;31m{List} : {List[y - 1]} <-> {List[y]}\033[0;31m")
                else:
                    break
            print(f"\033[0;32m{List} : {PreviousItem} <-> {CurrentItem}\033[0;32m")
        else:
            print(f"\033[0;33m{List}\033[0;33m : \033[0;32mNo swaps made\033[0;32m")
    return List

# Main program
UnsortedList = [random.randint(0, 100) for x in range(0, 25)] # Creates an unsorted list of 25 random numbers
SortedList = InsertionSort(UnsortedList) # Sorts the list using the insertion sort algorithm
# Prints the unsorted and sorted list
print("\n --- --- --- \n\n\033[0;33mThis is a insertion sort algorithm\033[0;33m")
print(f"""\033[0;31mUnsorted list : {UnsortedList}\033[0;31m
\033[0;32mSorted list : {SortedList}\033[0;32m""")
print("""\033[0;33mInsertion sort loops through a list
 - If less than previous item then it loops back and swaps it with the previous items until it reaches the start or is sorted
 - Continues the main loop to the end of list.\033[0;33m""")