# Program 1: Ask name and year of birth, tell age
def calculate_age():
    name = input("Enter your name: ")
    birth_year = int(input("Enter your year of birth: "))
    age = 2025 - birth_year
    print(f"Hello {name}, you are {age} years old.")

# Program 2: Extract car names from text
def extract_car_names():
    txt = 'LMaasleitbtui'
    car_names = txt[::2]
    print(f"Extracted car names: {car_names}")

# Program 3: String input operations
def string_operations():
    user_string = input("Enter a string: ")
    print(f"Length of the string: {len(user_string)}")
    print(f"Uppercase: {user_string.upper()}")
    print(f"Lowercase: {user_string.lower()}")

# Program 4: Check if string is palindrome
def is_palindrome():
    string = input("Enter a string: ")
    if string == string[::-1]:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

# Program 5: Count vowels and consonants
def count_vowels_consonants():
    string = input("Enter a string: ")
    vowels = 'aeiouAEIOU'
    v_count = sum(1 for char in string if char in vowels)
    c_count = sum(1 for char in string if char.isalpha() and char not in vowels)
    print(f"Vowels: {v_count}, Consonants: {c_count}")

# Program 6: Check if one string contains another
def check_contains():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the string to check: ")
    if string2 in string1:
        print(f"'{string2}' is found in '{string1}'.")
    else:
        print(f"'{string2}' is not found in '{string1}'.")

# Program 7: Replace word in a sentence
def replace_word():
    sentence = input("Enter a sentence: ")
    old_word = input("Word to replace: ")
    new_word = input("Replace with: ")
    print(f"Updated sentence: {sentence.replace(old_word, new_word)}")

# Program 8: First and last characters of a string
def first_last_characters():
    string = input("Enter a string: ")
    print(f"First character: {string[0]}, Last character: {string[-1]}")

# Program 9: Reverse a string
def reverse_string():
    string = input("Enter a string: ")
    print(f"Reversed string: {string[::-1]}")

# Program 10: Count words in a sentence
def count_words():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    print(f"Number of words: {len(words)}")

# Program 11: Check if a string contains digits
def contains_digits():
    string = input("Enter a string: ")
    if any(char.isdigit() for char in string):
        print("The string contains digits.")
    else:
        print("The string does not contain digits.")

# Program 12: Join list of words with a character
def join_words():
    words = input("Enter words separated by spaces: ").split()
    separator = input("Enter a separator: ")
    print(f"Joined string: {separator.join(words)}")

# Program 13: Remove all spaces from a string
def remove_spaces():
    string = input("Enter a string: ")
    print(f"String without spaces: {string.replace(' ', '')}")

# Program 14: Check if two strings are equal
def check_strings_equal():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    if string1 == string2:
        print("The strings are equal.")
    else:
        print("The strings are not equal.")

# Program 15: Create an acronym
def create_acronym():
    sentence = input("Enter a sentence: ")
    acronym = ''.join(word[0].upper() for word in sentence.split())
    print(f"Acronym: {acronym}")

# Program 16: Remove all occurrences of a character
def remove_character():
    string = input("Enter a string: ")
    char_to_remove = input("Enter the character to remove: ")
    print(f"Updated string: {string.replace(char_to_remove, '')}")

# Program 17: Replace vowels with a symbol
def replace_vowels():
    string = input("Enter a string: ")
    symbol = input("Enter a symbol to replace vowels: ")
    vowels = 'aeiouAEIOU'
    updated_string = ''.join(symbol if char in vowels else char for char in string)
    print(f"Updated string: {updated_string}")

# Program 18: Check if string starts and ends with specific words
def check_start_end():
    string = input("Enter a string: ")
    start_word = input("Starts with: ")
    end_word = input("Ends with: ")
    if string.startswith(start_word) and string.endswith(end_word):
        print("The string matches the conditions.")
    else:
        print("The string does not match the conditions.")

# Uncomment the functions below to run specific programs
# calculate_age()
# extract_car_names()
# string_operations()
# is_palindrome()
# count_vowels_consonants()
# check_contains()
# replace_word()
# first_last_characters()
# reverse_string()
# count_words()
# contains_digits()
# join_words()
# remove_spaces()
# check_strings_equal()
# create_acronym()
# remove_character()
# replace_vowels()
# check_start_end()
