######################################################################################
# Kevin R. Salger
# IS 640 Business Application Programming (Python)
# Homework 3, part 3.17
######################################################################################
"""
This program prints asterisks and spaces on the screen in a particular pattern.

"""

# VARS
Mynegai1 = 0
Mynegai2 = 0
Mynegai3 = 0
Mynegai4 = 0
Cyfrif1 = 0
Cyfrif2 = 0
Cyfrif3 = 0
Cyfrif4 = 0
# End VARS

# BEGIN
# Print the column headers
print (f'{"(a)":10}{"(b)":10}{"(c)":10}{"(d)":10}')

# Creates 10 rows
for RowNum in range (1,10):
    # 1st column of asterisks, 1 count up to 10
    for Mynegai1 in range (1,RowNum+1):
        print ("*",end="")
    # 1st column of spaces, 10 count down to 1
    for Cyfrif1 in range (1,12-(RowNum+1)):
        print (" ",end="")
    ###############################################
    # 2nd column of asterisks, 10 count down to 1
    for Mynegai2 in range (12-(RowNum+2),0,-1):
        print ("*",end="")
    # 2nd column of spaces, 1 count up to 10
    for Cyfrif2 in range (1,(RowNum+1)):     
        print (" ",end="")
    ###############################################
    #print ('!',end="")
    # 3rd column of spaces, 1 count up to 10
    for Cyfrif3 in range (1,RowNum):
        print (" ",end="")
    # 3rd column of asterisks, 1 count up to 10
    for Mynegai3 in range (12-(RowNum+1),1,-1):
        print ("*",end="")
    ###############################################
    # 4th column of spaces, 10 count down to 1
    for Cyfrif4 in range (12-(RowNum+1),1,-1):  
        print (" ",end="")
    # 4th column of asterisks, 1 count up to 10
    for Mynegai4 in range (1,(RowNum+1)):    # 
        print ("*",end="")
    ###############################################
    print ()    # Print the end of line/carriage return


# END