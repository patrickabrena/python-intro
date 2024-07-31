#the basic python data types

#numeric (integer, float, complex number)
#sequence
#dictionary
#boolean
#set

#to determine type of variable use type function ()

x = type("hello")
print(x)
#running the python file will return <class 'str'> in the terminal 

#sequence types are classed as container types that contain one or more of the same type






#3 main sequence types (Strings, Lists, Tuples)

#example of LIST sequence type
example_list = [1, 'hello', 4.5, "A"]
y = type(example_list)
print(example_list[1], y) 
#<class 'str'>
#hello <class 'list'>





#example of TUPLES sequence type (they are like lists execempt vals are immutable, difference is that tuple uses paraenthesis instead of square brackets)

example_tuple = (1, 'hello', 4.5, "A")
z = type(example_tuple)
print(example_tuple[1], z)




#example of DICTIONARY data type (they store data in key value pair structure)

ed = {'a':22, 'b':44.4} #'a' and 'b' are the keys and the integers are values
print(ed['a']) #prints 22 in the terminal





#BOOLEAN data types check the condition if true or false
print(type(True), type(False)) #will print <class 'bool'> <class 'bool'>



#SET data type is an unordered and non-indexed collection of non-repeated values (uses the curly braces)

example_set = {
    1, 'hello', 4.5, "A"
}

print(type(example_set)) # prints <class 'set'>