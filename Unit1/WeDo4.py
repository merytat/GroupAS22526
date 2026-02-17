# input
critA = int(input("Criteria A: "))
critB = int(input("Criteria B: "))
critC = int(input("Criteria C: "))
critD = int(input("Criteria D: "))

total = critD + critC + critB + critA
mypGrade = 0

# Selection (if statements for 8 paths)
if total >= 28:
    mypGrade = 7
elif total >= 23:
    mypGrade = 6
elif total >= 19:
    mypGrade = 5
elif total >= 15:
    mypGrade = 4
elif total >= 10:
    mypGrade = 3
elif total >= 6:
    mypGrade = 2
elif total >= 1:
    mypGrade = 1
else:
    print("Incorrect criteria Grades, try again")

# output
print("MYP Grade: ", mypGrade)

