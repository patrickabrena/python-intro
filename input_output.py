#examples of using explicit type casting
#using the int() function

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

sum = int(num1) + int(num2)
sum_str = str(sum)
print("num1 + num2 = " + sum_str)


#examples of string replacement in the print statement
str1 = input("what's your first name?: ")
str2 = input("What's your last name?: ")

print("Hello, {} {}".format(str1, str2) )