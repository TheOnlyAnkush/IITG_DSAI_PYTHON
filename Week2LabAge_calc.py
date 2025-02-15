
print("\nHi.. I am the 'Age Calculator'.")
print("If you will share your Date of Birth, I can tell your age")
print("Lets have a try.....\n")

#Input of date of birth from user
day=int(input("Enter Date (DD): "))
month=int(input("Enter Month (MM): "))
year=int(input("Enter Year (YYYY): "))

#Preparing DOB
from datetime import datetime
dob = datetime(year, month, day)

#importing of current date
today = datetime.today()

#Calculation of Age
difference = today - dob
age = difference.days // 365
print ("\nYour current age is:", age, "Yrs")

#Calculation of Next Birthday
next_bday = datetime(today.year, month, day)
if today > next_bday:
    next_bday = datetime(today.year+1, month, day)
bday_due = next_bday - today
print (bday_due.days, "Days left in your upcoming Birthday\n")
