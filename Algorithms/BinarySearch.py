# Binary search

# Binary search algorithm
def BinarySearch(SearchList, SearchItem):
    # Creates variables
    Index = -1
    Found = False
    LowerBound = 0
    UpperBound = len(SearchList) - 1
    # Performs binary search, loops until found or bounds cross/overlap
    while (not Found) and (LowerBound <= UpperBound):
        MidPoint = (LowerBound + UpperBound) // 2
        print(f"\033[0;34m --- --- --- \033[0;34m\n\033[0;33mLowerBound: {LowerBound} | MidPoint: {MidPoint} | UpperBound: {UpperBound}\033[0;33m")
        # Checks if item is in midpoint of range of search
        if SearchList[MidPoint] == SearchItem:
            Found = True
            Index = MidPoint
        # Checks if item is in left side of range of search and sets that side to the new range
        elif SearchList[MidPoint] > SearchItem:
            UpperBound = MidPoint - 1
            print(f"\033[0;33m{SearchItem} is < {SearchList[MidPoint]}.\033[0;33m")
        # Checks if item is in right side of range of search and sets that side to the new range
        elif SearchList[MidPoint] < SearchItem:
            LowerBound = MidPoint + 1
            print(f"\033[0;33m{SearchItem} is > {SearchList[MidPoint]}.\033[0;33m")
    print("\033[0;34m --- --- --- \033[0;34m")
    # Returns results of results
    if Found:
        print(f"\033[0;32m{SearchList} | {SearchItem} found in list.\033[0;32m")
    else:
        print(f"\033[0;031m{SearchList} | {SearchItem} not found at index {Index}\033[0;031m")
        
# Main
SearchingList = [x for x in range(0, 25)] # Creates an unsorted list of 25 random numbers
print("\n --- --- --- \n\n\033[0;33mThis is a binary search algorithm\033[0;33m")
print(f"\033[0;31mList : {SearchingList}\033[0;31m")
# Performs binary search
ItemToFind = int(input("\033[0;33mPlease enter an integer to search for from 0 to 24: \033[0;33m")) # Asks the user for an integer to search for
BinarySearch(SearchingList, ItemToFind) # Sorts the list using the insertion sort algorithm