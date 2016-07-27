name = "Zed A. Shaw" 
age = 35 # not a lie
height = 74 # inches
weight = 180 # pounds
eyes = "Blue"
teeth = "White"
hair = "brown"
height_in_centimeter = height / .3937

print "Let's talk about %r" % name # % is a python formatting character, e.g., %s, %d, %r 
print "He's %d centimeters tall." % height_in_centimeter
print "He's %d pounds heavy." % weight
print "Actually, that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right!
print "If I add %d, %d, and %d I'd get %d." % (age, height_in_centimeter, weight, age + height_in_centimeter + weight)
