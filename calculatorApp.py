# Python program A Simple Calculator App

from ast import main

# Function to add two numbers
def add(num1, num2):
	print("Processing addition..")
	return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
    print("Processing difference..")
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    print("Processing multiplication..")
    return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
    print("Processing division..")
    return num1 / num2

# Function to perform logic
def userManager(userSelection):
    if userSelection > 0 and userSelection < 5:
        number_1 = int(input("Enter first number: "))
        number_2 = int(input("Enter second number: "))
    print("/n")
    if userSelection == 1:
        print(number_1, "+", number_2, "=",
                        add(number_1, number_2))

    elif userSelection == 2:
        print(number_1, "-", number_2, "=",
                        subtract(number_1, number_2))

    elif userSelection == 3:
        print(number_1, "*", number_2, "=",
                        multiply(number_1, number_2))

    elif userSelection == 4:
        print(number_1, "/", number_2, "=",
                        divide(number_1, number_2))
    else:
        print("Invalid input")


# Function to handle User Experience post usage of the app
def userExperience(used):
    if used >=1 and used <=4:
        print("Hope you liked the phase one of the calculator app! :) ")
    else:
        print("Strongly regret the inconvenience, becoming better everyday!")


def main():
    name =""
    print("Welcome to a simple Calculator App.\n What can I call you ?")
    name = input()
    print("Hello "+name+ " Presenting you a simple calculator app, do try it. \nUsage follows:")
    print("Select any mathematical operation to perform from below list-\n" \
            "1. Add\n" \
            "2. Subtract\n" \
            "3. Multiply\n" \
            "4. Divide\n")

    # Take input from the user
    select = int(input("Select operations from 1, 2, 3, 4 :"))
    
    # handle the user request
    userManager(userSelection=select)
    
    # handle user experience
    userExperience(select)
    print("Program is now terminating ...")


# Initiating the app from here
if __name__ == '__main__':
    main()
    
