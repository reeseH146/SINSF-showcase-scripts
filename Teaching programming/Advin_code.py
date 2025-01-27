#This is fizzbuss. Takes one parameter, `x` that is the number to count up to. For multiples of 3 and 5 it outputs, "Fizz Buzz".For multiples of 3 only it outputs, "Fizz". For multiples of 5 only it outputs, "Buzz". For any other number it outputs the number.
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

#Cost problem, You enter an amount of people, the cost is people times 15 and if the people is above or equal to 6 then cost will be reduced by 5
def price (people):
    cost = people * 15
    if people >= 6:
        cost = cost - 5
    print (cost)

#Resteraunt, you enter the price you have to pay. People will take turns and pay their bill until the total price is 0.
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

#Character problem, you enter alphanumerical text then it turns if it is lower case or upper case or a mix between each.
def wording ():
    word = str(input("Enter a word: "))
    if word == word.upper():
        print ("Upper case")
    elif word == word.lower():
        print ("Lower case")
    else:
        print ("A bit of both!")


#Checkes the array and see how many number of colours and counts for each colour there is.
def array():
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

#Binary search code
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

#Bubblesort code
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

#Program which calculates total pay based on experience and miles
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


#You enter a number, this will be in bytes and you can convert it to GB, MB, KB or just bytes it self.
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
