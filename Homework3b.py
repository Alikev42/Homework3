######################################################################################
# Kevin R. Salger
# IS 640 Business Application Programming (Python)
# Homework 3, part 3.11
######################################################################################
"""12.8
This program calculates the gas mileage for each tankful based on the gallons of fuel
and the miles driven with that volume of fuel.  The final output
"""

# VARS

Mynegai = 0     # Mynegai = Welsh for "Index", "Index" is too close to a reserved word
Cyfrif = 0      # Cyfrif = Welsh for "Count"
TripGal = []    # List of unknown size.  Gallons used for one trip.
TripDist = []   # List of unknown size.  Distance traveled before filling the tank again.
TripMPG = []    # List of unknown size.  Holds MPG value for a tank
TotalDist = 0.0
TotalGal = 0.0
AvgMPG = 0.0    # Computes the average MPG for all trips.  Averages across all values of TripMPG.
# End VARS

# BEGIN
# Establishing dummy float values for lists
TripGal.append(0.0)
TripDist.append(0.0)
TripMPG.append(0.0)

# Begin While loop
while TripGal[Mynegai] != -1:
    TripGal[Mynegai] = input("Enter the gallons used (-1 to end): ")
    if float(TripGal[Mynegai]) == -1:
        break  # Exit the While loop, if user enters '-1'
    TripDist[Mynegai] = input("Enter the miles driven: ")
    
    # Calculating the MPG for a single tank, printing the result
    TripMPG[Mynegai] = float(TripDist[Mynegai])/float(TripGal[Mynegai])
    print (f'The miles/gallon for this trip was {TripMPG[Mynegai]:.8}')
    
    # Appending new dummy float values into the lists, and incrementing Mynegai by 1
    TripGal.append(0.0)
    TripDist.append(0.0)
    TripMPG.append(0.0)
    Mynegai = Mynegai + 1
# End of While loop    

# Overall MPG Calculation--Division of overall sums
for Cyfrif in range (Mynegai,0,-1):
    TotalDist = TotalDist + float(TripDist[Cyfrif-1])
    TotalGal = TotalGal + float(TripGal[Cyfrif-1])

AvgMPG = TotalDist/TotalGal
print (f'The overall average miles/gallon was {AvgMPG:.8}')

# END