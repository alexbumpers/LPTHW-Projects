from sys import argv

script, filename = argv

print "We're going to erase %r." % filename #let's user know we are erasing filename in this script
print "If you don't want that, hit CTRL-C (^C)." #gives directions to not delete filename
print "If you do want that, hit RETURN." #gives directions to delete filename
raw_input("?") #prompts for input RETURN or CTRL-C

print "Opening the file..." #string
target = open(filename, 'w') #defines target variable which opens the file, 'w' is the 'write' mode

print "Truncating the file. Goodbye!"
target.truncate() #truncates/shortens the file

print "Now I'm going to ask you for three lines." #prompts input for three lines
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "Now I'm going to write these to the file!"

target.write("%r'\n'%r'\n'%r'\n'" % (line1, line2, line3)) #writes lines 1-3 to the file on seperate lines

print "And finally, we close the file!" 
target.close() #closes file