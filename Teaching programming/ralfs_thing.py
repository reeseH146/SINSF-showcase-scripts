#Calculates the pay for a drone pilot depending on their total miles and years of experience#
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


#Converts Gigabytes.Megabytes and Kilobytes into Bytes#
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
    print(-1)
