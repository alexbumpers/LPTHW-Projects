formatter = "%r %r %r %r" #defines string of %rs

print formatter % (1, 2, 3, 4) #integers
print formatter % ("one", "two", "three", "four") #strings of numbers in word form
print formatter % (True, False, False, True) #prints true and false
print formatter % (formatter, formatter, formatter, formatter) #prints formatter string
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)