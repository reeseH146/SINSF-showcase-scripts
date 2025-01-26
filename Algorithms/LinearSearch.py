# Linear search
import random

# Linear search
def LinearSearch(ListToSearch, SearchItem):
    Count = 0
    Indexes = []
    Start = ""
    End = ""
    for x in range(len(ListToSearch)):
        print("\033[0;31m --- --- --- \033[0;31m")
        if ListToSearch[x] == SearchItem:
            Count += 1
            Indexes.append(x)
            print(f"\033[0;32m{ListToSearch} | {SearchItem} found at index {x}\033[0;32m")
        else:
            print(f"\033[0;31m{ListToSearch} | : {SearchItem} not found at index {x}\033[0;31m")
    print(" --- --- --- ")
    return Count, Indexes

# Main program
SearchingList = [random.randint(0, 100) for x in range(0, 25)] # Creates an unsorted list of 25 random numbers
print("\n --- --- --- \n\n\033[0;33mThis is a linear search algorithm\033[0;33m")
print(f"\033[0;31mList : {SearchingList}\033[0;31m")
# Performs linear search
ItemToFind = int(input("\033[0;33mPlease enter an integer to search for from 0 to 100: \033[0;33m")) # Asks the user for an integer to search for
Count, Indexes = LinearSearch(SearchingList, ItemToFind) # Sorts the list using the insertion sort algorithm
if not Count:
    print(f"\033[0;31mThe item {ItemToFind} has not been found in the list.\033[0;31m")
else:
    print(f"\033[0;33mThe item {ItemToFind} has been found {f"{Count} times" if Count != 1 else "once"}{f" at these indexes : {Indexes}." if Count != 1 else "."}\033[0;33m")