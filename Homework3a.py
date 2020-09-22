######################################################################################
# Kevin R. Salger
# IS 640 Business Application Programming (Python)
# Homework 3, part a
######################################################################################

import turtle

# VARS
pen = turtle.Pen()  # Create a turtle class member "pen"
# End VARS

######################################################################################
# BEGIN 
pen.up ()
pen.rt (90)
pen.fd (53)
pen.rt (90)
pen.fd (106)
pen.rt (45)
# End move to starting point

# Begin red half-square
pen.down ()
pen.color ("red")
pen.fd (75)
pen.rt (90)
pen.fd (150)
pen.rt (90)
pen.fd (75)
# End of red half-square

# Begin blue half-square
pen.color ("blue")
pen.lt (90)
pen.fd (75)
pen.rt (90)
pen.fd (150)
pen.rt (90)
pen.fd (75)
# End of blue half-square

# Return to center
pen.up ()
pen.home ()
pen.ht ()
turtle.done ()
# End of return to center

# END