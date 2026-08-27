import datetime

today = datetime.datetime.now()
day = int(input("Enter your birthdate day: "))
month = int(input("Enter your birthdate month: "))

birthdate = datetime.datetime(today.year,month,day)

if birthdate < today:
    birthdate = datetime.datetime(today.year+1,month,day)

daysLeft = birthdate - today
print("days left to your next birthday: " + str(daysLeft.days))