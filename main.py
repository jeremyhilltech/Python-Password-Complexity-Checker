import string
import getpass

def check_pwd():
    password=getpass.getpass("Enter Password: ")
    strength = 0
    remarks = ""
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == " ":
            wspace_count += 1
        else:
            special_count += 1

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1: 
        strength += 1
    if num_count >= 1: 
        strength += 1
    if wspace_count >= 1: 
        strength += 1
    if special_count >= 1: 
        strength += 1

    if strength == 1:
        remarks = "Extremely Weak Password!!! Please Change Immediately!"
    elif strength == 2:
        remarks = "Weak Password. Change ASAP To Avoid Security Risk."
    elif strength == 3:
        remarks = "Average Password. Consider Adding Complexity For Strength."
    elif strength == 4:
        remarks = "Good Password. Add More Complexity For Best Strength."
    elif strength == 5:
        remarks = "Strong Password. No Changes Recommended."

    print('Your Password Has: ')
    print(f"{lower_count} Lowercase Characters")
    print(f"{upper_count} Uppercase Characters")
    print(f"{num_count} Numeric Characters")
    print(f"{wspace_count} Whitespace Characters")
    print(f"{special_count} Special Characters")

    print(f'Your Password Complexity Is: {strength}')
    print(f'Message: {remarks}')

def ask_pwd(new_pwd=False):
    valid = False
    if new_pwd:
        choice=input('Do You Want To Enter Another Password? (y/n): ')
    else:
        choice=input('Do You Want To Check A Password? (y/n): ')
    while choice.lower() not in ["y","n"]:
        print('Invalid input, please enter "y" or "n".')
        choice = input("Do You Want To Check Another Password? (y/n): ")
    return choice.lower() == "y"
if __name__ == '__main__':
    print('+++ WELCOME TO THE PASSWORD COMPLEXITY CHECKER +++')
    print('This program will rate the strength of your password on a scale of 1 to 5.')
    print('You can use this tool check as many passwords as you like.')
    while True:
        ask_pw = ask_pwd()
        if ask_pw:
            check_pwd()
        else:
            print("Exiting program. Thank you for only using strong passwords!")
            break