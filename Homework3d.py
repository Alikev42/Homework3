######################################################################################
# Kevin R. Salger
# IS 640 Business Application Programming (Python)
# Homework 3, part 3.21
######################################################################################
"""
This program calculates the change using the fewest number of coins.

"""

# VARS
Dollar = 1.0
Price = 0.0
Change = 0.0
CountQ = 0
CountD = 0
CountN = 0
CountP = 0
# End VARS

# BEGIN
# Accepting user input
print ('The price of an item must be between $0.00 and $1.00.')
Price = input("Enter the price of the item: $")

# Limiting data entry between 0.00 and 1.00
while float(Price) < 0.0:
    print ('That value was below 0.0.')
    print ('Let\'s try that again, shall we?')
    Price = input("Enter the price of the item: $")    
while float(Price) > 1.0:
    print ('That value was above 1.0.')
    print ('Let\'s try that again, shall we?')
    Price = input("Enter the price of the item: $")

# Calculating the amount of Change to subdivide into coins
Change = float(Dollar)-float(Price)

# 0.00 <= Change <= 1.00
while Change > 0.01:                # Run & rerun this until no more change remains
    while Change >= 0.25:           # As long as Change is greater than a quarter, run this loop
        Change -= 0.25              # Subtract 0.25 
        Change = round(Change, 2)   # *** Correction for Python accumulated math error ***
        CountQ += 1                 # Increment count of quarters
    while Change >= 0.10:           # As long as Change is greater than a dime, run this loop
        Change -= 0.10              # Subtract 0.10
        Change = round(Change, 2)   # *** Correction for Python accumulated math error ***
        CountD += 1                 # Increment count of dimes
    while Change >= 0.05:           # As long as Change is greather than a nickel, run this loop
        Change -= 0.05              # Subtract 0.05
        Change = round(Change, 2)   # *** Correction for Python accumulated math error ***
        CountN += 1                 # Increment count of nickels
    while Change >= 0.01:           # As long as Change is greater than a penny, run this loop
        Change -= 0.01              # Subtract 0.01
        Change = round(Change, 2)   # *** Correction for Python accumulated math error ***
        CountP += 1                 # Increment count of pennies
 
print ('Your change is:')
if CountQ > 0:                      # Test for Quarter count
    print (CountQ,' quarters')      # Print Quarter count
if CountD > 0:                      # Test for Dime count
    print (CountD,' dimes')         # Print Dime count
if CountN > 0:                      # Test for Nickel count
    print (CountN,' nickels')       # Print Nickel count
if CountP > 0:                      # Test for Penny count
    print (CountP,' pennies')       # Print Penny count
# END