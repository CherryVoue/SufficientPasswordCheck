from getpass import getpass

def strength_check(password):
    upper = 0
    lower = 0
    nums = 0
    specialChars = ["#","!","$","_"]

    if len(password) >= 9:
        if any(char in password for char in specialChars):
            for char in password:
                if char.isdigit():
                    nums+=1
                elif char.isupper():
                        upper+=1
                elif char.islower():
                        lower+=1
    return (upper > 0 and lower > 0 and nums > 0)
                
    
def main():
    password = ""
    while not strength_check(password):
        print("Please enter a password that contains the following characteristics: at least 9 characters, includes uppercase and lowercase letters, includes at least 1 number, contains one of the following characters: #, !, $, _")
        password = getpass()
    print("Password strength is sufficient")

if __name__ == "__main__":
    main()
