#Extremely simgle command which uses a basic syntax "print" to make a text or a number appear on the screen#
print("Hello World")
#If we wanted to print(display) a number, we have to remove the quotation marks as that is used for text or a string of alphabetic characters#
#This would dicplay the number 34  on the command box
print(34)
#We can further expand uppon this idea by using commands that require an input from the user which we can later use if we wanted to, in this case, we use "X"#
#as a place to store the user input which we can change later if we wanted which is why its called a variable#
x=input("What is your favourite animal?:")
#We can create a loop which goes through a series of numbers and prints them out#
#We use i as a place to store the value of the current number from our loop as it starts at 0 and ends at 9. The number increases by 1 each time so 0 becomes 1 and then 1 becomes 2 until it reaches 9, as its incereasing,
#the programme is printing each of the values, so before 0 becomes 1, the 0 is printed and then it prints 1 as 0 beconmes 1 and so on
for i in range(0,9):
    print(i)
#Calculates the pay for a drone pilot depending on their total miles and years of experience by using functions where we can give it a value and it will perform the calculation what is in the function and return a value afteer the calcualtions#
experience=float(input("Enter your years of experience:"))
miles=float(input("Enter miles flown:"))
totalpay=0

def less_two_years():
    totalpay=((0.45*miles)*100)+150
    return totalpay

def less_than_five():
    totalpay=((0.65*miles)*100)+150
    return totalpay

def more_than_five():
    totalpay=((0.85*miles)*100)+150
    return totalpay

if experience>2:
    print(less_two_years())

elif experience<2 and experience>= 5:
    print(less_than_five())

else:
    print(more_than_five())


#Converts Gigabytes.Megabytes and Kilobytes into Bytes by using math and storing them as a value. The value that is displayed also depends on what size of storage that is inputed which is separated with the use of 
# If and elif statements which alows us to use diffirent inputed values for diffirent mathematical opparations.
size=input("Gigabyte , Megabyte or Kilobyte ?:")
amount=float(input("How many do you have?:"))

if size=="Gigabyte":
    value=(amount*1024*1024*1024*8)
    print(value,"bytes")

elif size=="Megabyte":
    value=(amount*1024*1024*8)
    print(value,"bytes")

elif size=="Kilobyte":
    value=(amount*1024*8)
    print(value,"bytes")

else:
    print("Invalid Size")
