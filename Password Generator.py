import _random
import sys
"""
Random password generator with a command-line search.
Based on user preferred characters and password length.
Character set handling. User input handling. GUI interface using PyQt. 
Allow users to copy password to clipboard for convenience. 
Enable users to customize password generation.
"""

# We want the user to create a password using one of these characters
    
uppercase_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_characters = "abcdefghijklmnopqrstuvwxyz"
symbols = "!#$%&+="
numbers = "0123456789"

password = uppercase_characters + lowercase_characters + symbols + numbers
password = input()  # This will allow the user to enter their preferred password.

# The password should have a minimum length or number of characters.
length = 6

"""
How do we ensure that a user knows they must enter an uppercase character, lowercase character,
one or more digits and a symbol? There should be a message after each input to ensure that the password
#meets security guidelines.
"""

# Use an if statement as a solution.
if len(password) >= length and password in password:
    print("\033[32mPassword Correct!\033]")
else:
    print("\033[31mError! Please enter a password with six characters or more, including a number and a symbol.\033]an")






























