def fizzbus():
    x = int(input("Enter a number: "))
    for i in range (x+1):
        if i == 0:
            print (i)
        elif i % 3 == 0 and i % 5 == 0:
            print ("Fizz Buzz")
        elif i % 3 == 0:
            print ("Fizz")
        elif i % 5 == 0:
            print ("Buzz")
        elif i == 0:
            print (i)
        else:
            print (i)

#Cost problem
def price (people):
    cost = people * 15
    if people >= 6:
        cost = cost - 5
    print (cost)
    return cost

#Resteraunt problem
def resteraunt():
    pricex = float(input("Enter the price: "))
    while pricex != 0:
        pay = float(input("Enter the pay: "))
        pricex = pricex - pay
        print (f"You have: {pricex} left to pay.")
        if pricex <= 0:
            print ("Your change is: ", pricex)
            break
    print ("Bill paid, thank you!")

#Character problem
def wording ():
    word = str(input("Enter a word: "))
    if word == word.upper():
        print ("Upper case")
    elif word == word.lower():
        print ("Lower case")
    else:
        print ("A bit of both!")


def array():
    #Creating an array
    array = ["Red", "Blue", "Green", "Yellow", "Blue", "Green", "Yellow", "Red"]
    blue_counter = 0
    red_counter = 0
    green_counter = 0
    yellow_counter = 0
    x = len(array)
    for i in range(x):
        if "Blue" == array[i]:
            blue_counter += 1
            print ("Blue counters:", blue_counter)
        elif "Green" == array[i]:
            green_counter += 1
            print ("Green counters: ", green_counter)
        elif "Yellow" == array[i]:
            yellow_counter += 1
            print ("Yellow counters:", yellow_counter)
        elif "Red" == array[i]:
            red_counter += 1
            print ("Red counters:", red_counter)
    print ("I cannot be asked to print the final result so you will see them incrementing to the final value instead")

def bigman():
    group = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    found = False
    first = 0
    last = len(group) -1

    search = input("Enter president: ")
    while first <= last and found == False:
        midpoint = (first + last)//2
        if group[midpoint]  == search:
            found = True
        else:
            if group[midpoint] < search:
                first = midpoint + 1
                print(midpoint)
            else:
                last = midpoint - 1
                print(midpoint)
    if found == True:
        print(search, "has been found at", midpoint)
    else:
        print("Not found")

def bubblesort():
    presidents = ["Obama", "Trump", "Biden", "Boris", "Rishi", "Starmer"]
    swapped = True
    n = len(presidents)
    while n>0 and swapped == True:
        swapped = False
        n = n-1
        for i in range(0,n):
            if presidents[i] > presidents[i+1]:
                temp = presidents[i]
                presidents[i] = presidents[i+1]
                presidents[i+1] = temp
                swapped = True

def salary(experience, miles):
    if experience < 2:
        totalpay = 150 + (0.45*miles)
        print(totalpay)
    elif experience >= 2 and experience <5:
        totalpay = 150 + (0.65*miles)
        print(totalpay)
    else:
        totalpay = 150 + (0.85*miles)
        print(totalpay)


def calculates():
    number = int(input("Enter the value in bytes: "))
    measurement = str(input("Enter what form you want it in: ")).upper()
    if measurement == "GIGABYTE":
        value = number / ( 1024 * 1024 * 1024 * 8)
    elif measurement == "MEGABYTE":
        value = number / ( 1024 * 1024 * 8)
    elif measurement == "KILOBYTE":
        value = number / (1024 * 8)
    elif measurement == "BYTES":
        value = number
    print (value)
