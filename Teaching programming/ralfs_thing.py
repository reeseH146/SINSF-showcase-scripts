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
