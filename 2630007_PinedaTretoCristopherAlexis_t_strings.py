# Front Page
# Student: Cristopher Alexis Pineda Treto
# Student ID: 2630007
# Group: 3
# Teacher: M.C Carlos Antonio Tovar Garcia
 
# =============================================================================
# EXECUTIVE SUMMARY
# A string in Python is a data type called str. It is a sequence of characters.
# Strings are immutable, so we cannot change them. Any change creates a new string.
# With strings we can join text (+), get the length (len()), take parts of the
# text (slicing), search text (find, in) and replace text (replace).
# It is important to validate and normalize the input text. Users can write extra
# spaces, capital letters or wrong formats in emails, names and passwords.
# If we do not clean and check the text, the program can fail or save bad data.
# This document has 6 problems. For each one, it explains the description, the
# inputs and outputs, and the validations used.
# It also uses string methods in the code and shows 3 test cases for each problem
# (normal, border and error).
 
# =============================================================================
# GOOD PRACTICES
# - Strings are immutable: any change creates a new string.
# - Clean the input with strip() and lower() before comparing it.
# - Do not use "magic numbers": use constants with clear names.
# - Use string methods instead of writing the same logic again.
# - Validate first that the text is not empty, then validate the format.
# - Use clear variable names and clear error messages.
# To test each problem, change the value of the first variable. The border and
# error values are written in comments below each problem.
 
# =============================================================================
# Problem 1: Full name formatter
# Description: Formats a full name and displays the initials.
# Inputs: A person's full name
# Outputs: Formatted name and initials
# Validations: The name cannot be empty and must have at least 2 words
# Normal: "anahi treto" -> Anahi Treto, A.T.
# Border: "Anahi T" -> Anahi T, A.T.
# Error: "   " -> Error: invalid input
#        "anahi" -> Error: enter at least two words
 
full_name = "anahi treto"
# full_name = "Anahi T"    # border case
# full_name = "   "        # error case
full_name = " ".join(full_name.strip().split())
 
if len(full_name) == 0:
    print("Error: invalid input")
else:
    name_parts = full_name.split()
 
    if len(name_parts) < 2:
        print("Error: enter at least two words")
    else:
        formatted_name = full_name.title()
        initials = ""
 
        for name in name_parts:
            initials += name[0].upper() + "."
 
        print("Formatted name:", formatted_name)
        print("Initials:", initials)
 
print()
 
# =============================================================================
# Problem 2: Simple email validator
# Description: Checks if an email has a basic correct format and shows the domain.
# Inputs: An email text
# Outputs: Valid email (true or false) and the domain if it is valid
# Validations: The text cannot be empty, it must have exactly one "@", no spaces,
#              something before the "@" and at least one "." after the "@"
# Normal: "anahi.treto@mail.com" -> Valid email: true, Domain: mail.com
# Border: "a@b.c" -> Valid email: true, Domain: b.c
# Error: "anahi.treto@@mail.com" -> Valid email: false
#        "   " -> Error: invalid input
 
email_text = "anahi.treto@mail.com"
# email_text = "a@b.c"                   # border case
# email_text = "anahi.treto@@mail.com"   # error case
email_text = email_text.strip()
 
if len(email_text) == 0:
    print("Error: invalid input")
else:
    if email_text.count("@") != 1 or " " in email_text:
        print("Valid email: false")
    else:
        at_index = email_text.find("@")
        domain = email_text[at_index + 1:]  # everything after the "@"
 
        if at_index == 0 or "." not in domain:
            print("Valid email: false")
        else:
            print("Valid email: true")
            print("Domain:", domain)
 
print()
 
# =============================================================================
# Problem 3: Palindrome checker
# Description: Checks if a phrase reads the same forward and backward,
#              ignoring spaces and uppercase or lowercase letters.
# Inputs: A phrase
# Outputs: Normalized text and Is palindrome (true or false)
# Validations: The phrase cannot be empty and must have at least 3 letters
#              after removing the spaces
# Normal: "Anita lava la tina" -> Is palindrome: true
# Border: "Ala" -> Is palindrome: true (exactly 3 letters)
# Error: "   " -> Error: invalid input
#        "Anahi Treto" -> Is palindrome: false
 
MIN_PALINDROME_LENGTH = 3
 
phrase = "Anita lava la tina"
# phrase = "Ala"   # border case
# phrase = "   "   # error case
clean_text = phrase.strip().lower().replace(" ", "")
 
if len(clean_text) < MIN_PALINDROME_LENGTH:
    print("Error: invalid input")
else:
    reversed_text = clean_text[::-1]  # the same text, backward
    print("Normalized:", clean_text)
 
    if clean_text == reversed_text:
        print("Is palindrome: true")
    else:
        print("Is palindrome: false")
 
print()
 
# =============================================================================
# Problem 4: Sentence word stats
# Description: Splits a sentence into words and shows the word count, the first
#              and last word, and the shortest and longest word.
# Inputs: A sentence
# Outputs: Word count, first word, last word, shortest word and longest word
# Validations: The sentence cannot be empty and must have at least one word
# Normal: "  Anahi Treto likes red apples  " -> 5 words, first Anahi, last apples,
#         shortest red, longest apples
# Border: "Anahi" -> 1 word, and all the other results are Anahi
# Error: "   " -> Error: invalid input
# Note: if two words have the same length, the first one is kept.
 
sentence = "  Anahi Treto likes red apples  "
# sentence = "Anahi"   # border case
# sentence = "   "     # error case
words = sentence.strip().split()
 
if len(words) == 0:
    print("Error: invalid input")
else:
    shortest_word = words[0]
    longest_word = words[0]
 
    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word
        if len(word) > len(longest_word):
            longest_word = word
 
    print("Word count:", len(words))
    print("First word:", words[0])
    print("Last word:", words[-1])
    print("Shortest word:", shortest_word)
    print("Longest word:", longest_word)
 
print()
 
# =============================================================================
# Problem 5: Password strength classifier
# Description: Classifies a password as weak, medium or strong.
# Rules:
#   Strong: 8 or more characters, with an uppercase letter, a lowercase letter,
#           a digit and a symbol (a character that is not a letter or a digit).
#   Medium: 8 or more characters, with uppercase and lowercase letters, or a digit.
#   Weak: any other case (too short or too simple).
# Inputs: A password
# Outputs: Password strength (weak, medium or strong)
# Validations: The password cannot be empty (or only spaces)
# Normal: "AnahiTreto#2026" -> Password strength: strong
# Border: "AnahiT12" -> Password strength: medium (exactly 8 characters, no symbol)
# Error: "" -> Error: invalid input
 
MIN_LENGTH = 8
 
password_input = "AnahiTreto#2026"
# password_input = "AnahiT12"   # border case
# password_input = ""           # error case
 
if len(password_input.strip()) == 0:
    print("Error: invalid input")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False
 
    for character in password_input:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_digit = True
 
        if not character.isalnum():
            has_symbol = True
 
    if len(password_input) < MIN_LENGTH:
        strength = "weak"
    elif has_upper and has_lower and has_digit and has_symbol:
        strength = "strong"
    elif (has_upper and has_lower) or has_digit:
        strength = "medium"
    else:
        strength = "weak"
 
    print("Password strength:", strength)
 
print()
 
# =============================================================================
# Problem 6: Product label formatter
# Description: Creates the label "Product: <NAME> | Price: $<PRICE>" with exactly
#              30 characters. A short label is filled with spaces at the end
#              and a long label is cut.
# Inputs: A product name and a price
# Outputs: The label between quotes, to see the spaces
# Validations: The name cannot be empty and the price must be a positive number
# Normal: "Pen", 2.5 -> Label: "Product: Pen | Price: $2.5    "
# Border: "Anahi Treto Mechanical Keyboard", 1299.99 -> Label: "Product: Anahi Treto Mechanica"
# Error: "Pen", -3 -> Error: invalid input
 
LABEL_LENGTH = 30
 
product_name = "Pen"
price_value = 2.5
# product_name = "Anahi Treto Mechanical Keyboard"   # border case
# price_value = 1299.99                              # border case
# price_value = -3                                # error case
product_name = product_name.strip()
price_text = str(price_value).strip()
 
# replace(".", "", 1) removes one point so isdigit() can check a decimal number
if (len(product_name) == 0
        or not price_text.replace(".", "", 1).isdigit()
        or float(price_text) <= 0):
    print("Error: invalid input")
else:
    label = "Product: " + product_name + " | Price: $" + price_text
    label = label[:LABEL_LENGTH]                       # cut if it is too long
    label = label + " " * (LABEL_LENGTH - len(label))  # fill if it is too short
    print('Label: "' + label + '"')
 
# =============================================================================
# CONCLUSIONS
# Strings are very important because almost all the data that a user types is text.
# Methods like strip() and lower() are useful to clean the text before using it.
# The split() method is good to separate words and join() is good to put them together.
# It is important to normalize the text before comparing it. For example, in the
# palindrome problem we remove spaces and use lower() to compare correctly.
# Validations avoid errors and bad data, like empty names, wrong emails and negative prices.
# I learned that strings are immutable, so methods like replace() and title()
# return a new string. I also learned that slices like [::-1] and [:30] are
# a simple way to reverse and cut text.
 
# =============================================================================
# REFERENCES
# 1) Python documentation - Built-in Types: Text Sequence Type - str
#    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# 2) Python documentation - String Methods
#    https://docs.python.org/3/library/stdtypes.html#string-methods
# 3) Python documentation - Tutorial: An Informal Introduction (Strings)
#    https://docs.python.org/3/tutorial/introduction.html
# 4) Real Python - Strings and Character Data in Python
#    https://realpython.com/python-strings/
# 5) W3Schools - Python Strings
#    https://www.w3schools.com/python/python_strings.asp
#=============================================================
#SPECIAL MESSAGE 
#I LOVE ANAHI AND PYTHON
#GIVE A 10 CHARLY MERCURY