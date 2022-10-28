# Program Name: lab9_stringManip.py
# Course: IT1114/Section 1
# Student Name: Tristen Rivera-Steinkritz
# Assignment Number: Lab9
# Due Date: 11/6/2022
# Purpose: 
# Resources: https://stackoverflow.com/questions/19859282/check-if-a-string-contains-a-number, https://www.geeksforgeeks.org/python-test-if-string-contains-element-from-list/, 

from getpass import getpass

def strength_check(password):
    upper = 0
    lower = 0
    nums = 0
    specialChars = ["#","!","$","_"]
    if len(password) >= 9:
        if any(char in specialChars for char in test_list):
            for char in password:
                if char.isdigit():
                    nums+=1
                elif char.upper() == char:
                    upper+=1
                elif char.lower() == char:
                    lower+=1
    return (upper > 0 and lower > 0 and nums > 0
                
    
def main():
    password = None
    while not strength_check(password):
            password = input("Please enter a password that contains the following characteristics: at least 9 characters, includes uppercase and lowercase letters, includes at least 1 number, contains one of the following characters: #, !, $, _ \nPassword:


if __name__ == "__main__":
    main()