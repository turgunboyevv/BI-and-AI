# Program 1: Check if username and password are not empty
def check_username_password():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username and password:
        print("Both username and password are provided.")
    else:
        print("Username or password cannot be empty.")

# Program 2: Check if two numbers are equal
def check_numbers_equal():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num1 == num2:
        print("The numbers are equal.")
    else:
        print("The numbers are not equal.")

# Program 3: Check if a number is positive and even
def check_positive_even():
    num = int(input("Enter a number: "))
    if num > 0 and num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is not positive and even.")

# Program 4: Check if three numbers are all different
def check_all_different():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    if num1 != num2 and num1 != num3 and num2 != num3:
        print("All three numbers are different.")
    else:
        print("Not all numbers are different.")

# Program 5: Check if two strings have the same length
def check_same_length():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    if len(string1) == len(string2):
        print("Both strings have the same length.")
    else:
        print("The strings have different lengths.")

# Program 6: Check if a number is divisible by both 3 and 5
def check_divisible_by_3_and_5():
    num = int(input("Enter a number: "))
    if num % 3 == 0 and num % 5 == 0:
        print("The number is divisible by both 3 and 5.")
    else:
        print("The number is not divisible by both 3 and 5.")

# Program 7: Check if the sum of two numbers is greater than 50
def check_sum_greater_than_50():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num1 + num2 > 50:
        print("The sum of the two numbers is greater than 50.")
    else:
        print("The sum of the two numbers is not greater than 50.")

# Program 8: Check if a number is between 10 and 20 (inclusive)
def check_between_10_and_20():
    num = int(input("Enter a number: "))
    if 10 <= num <= 20:
        print("The number is between 10 and 20 (inclusive).")
    else:
        print("The number is not between 10 and 20.")

# Uncomment the functions below to run specific programs
# check_username_password()
# check_numbers_equal()
# check_positive_even()
# check_all_different()
# check_same_length()
# check_divisible_by_3_and_5()
# check_sum_greater_than_50()
# check_between_10_and_20()