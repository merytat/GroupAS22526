# program to calculate cost of a trip

# read input
print("Trip Calculator")
destination = input("Enter destination: ")
noNights = int(input("Enter No. of Nights: "))
hotelPerDay = float(input("Enter cost of hotel per day: "))
flightCost = float(input("Enter the cost of flights: "))
mealsPerDay = float(input("Enter cost of meals per day: "))
transCost = float(input("Enter the cost of transportation per day: "))
noPeople = int(input("Enter no of people traveling: "))

# calculations
subTotalHotel = hotelPerDay * noPeople * noNights
subTotalFlight = flightCost * noPeople
subTotalMeals = mealsPerDay * noPeople * noNights
subTotalTrans = transCost * noPeople * noNights

totalCost = subTotalTrans + subTotalMeals + subTotalHotel + subTotalFlight

perHotel = (subTotalHotel / totalCost) * 100

# output
print()
print("Trip Budget for " + destination)
print("Item \t Subtotal \t Percentage")
print("Hotel \t", subTotalHotel, "\t", perHotel)


















