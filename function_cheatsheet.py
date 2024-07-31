# list of some build in functions

#print function
print("hello")

#input function
#this function lookds for the default input device, your keyboard, and captures the value.
#This value can then be assigned or used
print("Where do you live?")
location = input() # when i run the build and input a string it will return "so you live in [whatever my input was]"
print("so you live in " + location)

#len function
#This function returns the length or the count of elements contained within the structure it is applied on.
#This may be a string, array, list, tuple, dictionary, or any sequence
len("Hello")
#5

#str function
#This function can be used to convert the provided value into a string
str(55)
#'55'

#int function
#This function can be used to convert the provided value into an int
int('75')
#75

#float function
#This function can be used to convert the provided value into a float
some_int = 10
float(some_int)
#10.0


#CREATING FUNCTIONS
#functions in python require a keyword to define them ;def followed by an identifier.
#this forms the function signature.
#the body of th function contains the code to run when the function is called