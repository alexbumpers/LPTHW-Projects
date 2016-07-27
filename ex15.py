from sys import argv

script, filename = argv #arguments to call in powershell

txt = open(filename) #defines variable 'txt', which opens the filename argument

print "Here's your file %r:" % filename # String saying here's your file with the filename filled in
print txt.read() #reads the file in the txt variable

print "Type the filename again: " #prompts for the filename again
file_again = raw_input("> ") #allows user to input filename again, defines var file_again

txt_again = open(file_again) #defines txt_again, opens file_again

print txt_again.read() #prints txt_again

txt.close()
txt_again.close()