# program to calculate the total
# cost of eggs

# read input
numEggs = int(input("Number of eggs: "))
pricePerDozen = float(input("Price per dozen: "))
pricePerEgg = float(input("Price per egg: "))

# Calculate num dozens
# eggs // 12 - integer division
numDozens = numEggs // 12

# Calculate cost of dozens
# multiple No of dozens * price per dozen
costOfDozens = pricePerDozen * numDozens

# Calculate left over eggs
# eggs % 12 - reminder division
leftOverEggs = numEggs % 12

# calculate cost of left over eggs
# multiple ind eggs * price per egg
leftOverCost = pricePerEgg * leftOverEggs

# Calculate total cost
# add price of dozens + price of ind eggs
totalCost = round((costOfDozens + leftOverCost),4)

# output results
print("Total number dozens: ", numDozens)
print("Total price: ", totalCost)