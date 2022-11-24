import ast
import time
account = {}
i = 0
def option1():
    global account
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    confirm_password = input("Please confirm your password: ")
    if password == confirm_password:
        try:
            with open("Account.txt") as r:
                file = r.read()
                dictionary = ast.literal_eval(file)
                account = dictionary
        except:
            pass
        account[username] = password
        print("Your account has been created.")
        with open("Account.txt", "w") as w:
            w.write(str(account))
    else:
        print("Passwords don't match try again")

def option2():
    global account
    with open("Account.txt") as r:
        file = r.read()
        dictionary = ast.literal_eval(file)
        user = input("Enter your useranme: ")
        password = input("Enter your password: ")
        try:
            if dictionary[user] == password:
                print("\n")
                print("You have been logged in. Welcome {}.".format(user))
        except:
            print("Account not found.")
            
def option3():
    global account
    username = input("Enter your username: ")
    password = input("Enter your CURRENT password: ")
    try:
        if account[username] == password:
            new_password = input("Enter your NEW password: ")
            account[username] = new_password
            with open("Account.txt", "w") as w:
                w.write(str(account))
            print("Password changed successfully.")
        else:
            print("Passwords don't match")
    except:
        print("An error has occurred")
        
def option4():
    try:
        username = input("Enter your username of the account you want to delete: ")
        password = input("Enter the password password: ")
        with open("Account.txt") as r:
            file = r.read()
            dictionary = ast.literal_eval(file)
            if dictionary[username] == password:
                dictionary.pop(username)
                print("Account removed")
                account = dictionary

        with open("Account.txt", "w") as w:
            w.write(str(account))
    except:
        print("An error has occurred")

while True:
    file = open("Account.txt", "a")
    file.close()
    try:
        with open("Account.txt") as r:
            file = r.read()
            dictionary = ast.literal_eval(file)
            account = dictionary
    except:
        pass
    print("What would you like to do? Enter a number (1-5)")
    print("1 - Create Account")
    print("2 - Login")
    print("3 - Change Password")
    print("4 - Delete Account")
    print("5 - Quit")
    try:
        option = int(input("Enter your option: "))
        if option != 1 and option != 2 and option != 3 and option != 4 and option != 5 and option != 6:
            print("\nPlease entire a valid integer (1-5)")
            time.sleep(2)
            print("\n")
        else:
            if option == 1:
                option1()
            if option == 2:
                option2()
            if option == 3:
                option3()
            if option == 4:
                option4()
            if option == 5:
                print("Thanks for playing. Quiting now.")
                break
            
    except:
        print("\nPlease entire a valid integer (1-5)")
        time.sleep(2)
        print("\n")
    

