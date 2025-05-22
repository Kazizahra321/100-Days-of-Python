# Exercise84: Regular Expressions in Python

# Regular expression is a sequence of characters that defines a search pattern.
# In python they are handled using a builtin re module.
# These are used for searching, atching or replacing text based on specific patterns.


# Basic functions in re Module

# re.match(): Checks for match only at the beginning of a string.
# re.search(): Searches the entire string for a match.
# re.findall(): Returns a list of all matches.
# re.sub(): Replaces one or more matches with a string.
# re.split(): Splits a string by the occurrences of a pattern

# Pattern Syntax (Meta Characters)
# . : Any character except newline
# ^ :  
# $ :
# * :
# + :
# ? :
# {n} :
# [] :
# ` :
# \d :
# \w :
# \s :

# Examples

import re
 
 # check if a string starts with "Hello"
text = "Hello, madam"
if re.match(r'^Hello', text):
    print("Starts with Hello")

# Find all numbers in a string
text = "There are 3 apples and 5 bananas"
numbers = re.findall(r'\d+', text)
print(numbers)

# Validate all email address
email ="abc@gmail.com"
if re.match(r'^[\w.-]+@[\w.-]+\.\w+$',email):
    print("Valid email")
else:
    print("Invalid email")

# Replace all spaces with dashes
text = "Helloo  Ladyy"
newtext = re.sub(r'\s', '-',text)
print(newtext)