# To the Util Class add dayOfWeek static function that takes a date as input and
# prints the day of the week that date falls on. Your program should take three
# command­line arguments: m (month), d (day), and y (year). For m use 1 for January,
# 2 for February, and so forth. For output print 0 for Sunday, 1 for Monday, 2 for
# Tuesday, and so forth. Use the following formulas, for the Gregorian calendar (where
# / denotes integer division):
# y0 = y − (14 − m) / 12
# x = y0 + y0/4 − y0/100 + y0/400
# m0 = m + 12 × ((14 − m) / 12) − 2
# d0 = (d + x + 31m0/ 12) mod 7

month = int(input("Enter Month in integer(1 to 12): "))
date = int(input("Enter the Date: "))
year = int(input("Enter the year: "))

class Calendar:
    def __init__(self,month,day,year):
        self.month = month
        self.day = day
        self.year = year
    
    def dayOfWeek(self):
        y = self.year - (14-self.month)//12
        x = y + y//4 - y//100 + y//400
        m = self.month + 12*((14 - self.month)//12)-2
        d = (self.day + x + 31*m//12)%7
        return d


day = Calendar(month,date,year)

if day.dayOfWeek()==0:
    print("Sunday")
elif day.dayOfWeek()==1:
    print("Monday")
elif day.dayOfWeek()==2:
    print("Tuesday")
elif day.dayOfWeek()==3:
    print("Wednesday")
elif day.dayOfWeek()==4:
    print("Thursday")
elif day.dayOfWeek()==5:
    print("Friday")
elif day.dayOfWeek()==6:
    print("Saturday")    
