import time


# declare menu function
def menu():
    # take users input for their choice
    choice = input("1. Create an account\n"
                   "2. Login\n"
                   "3. Exit\n"
                   "Enter 1, 2 or 3 for desired option: ")
    # Check which option the user chose
    if choice == "1":
        # call the createAccount function
        createAccount()
    elif choice == "2":
        # Call the login function
        login()
    elif choice == "3":
        # Call the exit program function
        exitProg()
    else:
        # Print error message and call the menu function again
        print("\nInvalid option. Try again.\n")
        menu()


# Declare the createAccount function
def createAccount():
    # Get the users input for email, password and confirmedPassword
    email = input("\nPlease enter your email: ")
    password = input("Please enter your password: ")
    confirmedPassword = input("Please reenter your password: ")

    while email.strip() == "" or password.strip() == "" or confirmedPassword.strip() == "":
        print("\nInformation incorrect, please try again")
        email = input("\nPlease enter your email: ")
        password = input("Please enter your password: ")
        confirmedPassword = input("Please reenter your password: ")

    # Store the opened text file in the variable f
    f = open('info.txt', "r")
    # Iterate through the text file
    for newMail in f:
        # Split the line read from the txt file at the :
        x = newMail.split(":")
        # Check if the email already exists by using the first part of the spit string (Which is the email in the text file)
        if x[0] == email:
            # Print message and send the user to the login page by calling the login function cause the email already exists
            print("Account already exists.\nSending you to login page")
            login()

    # Check if the passwords inputted match
    if password == confirmedPassword:
        print("Creating Account...")
    else:
        # Keep checking until the passwords match
        while not password == confirmedPassword:
            print("Passwords don't match, try again")
            password = input("Please enter your password: ")
            confirmedPassword = input("Please re-enter your password: ")

    # Append onto the info.txt file with the format (email:password)
    with open('info.txt', "a") as file:
        file.write("\n" + email + ":" + password)

    # Print success message and return to the menu
    print("\nAccount, " + email +" has been created!\nSending you back to the main menu\n")
    menu()


# Declare the lgoin method
def login():
    # Get the users input
    print("\nLogin Page")
    email = input("\nPlease enter your email: ")
    password = input("Please enter your password: ")

    # Keep checking until the input fields are not empty
    while email.strip() == "" or password.strip() == "":
        print("\nInformation incorrect, please try again")
        email = input("\nPlease enter your email: ")
        password = input("Please enter your password: ")

    correct = False
    # Store the opened text file in the variable f
    f = open('info.txt', "r")
    # Iterate through the text file
    for newMail in f:
        # Split the line of the text file at the : (Seperates email and password)
        x = newMail.split(":")
        # Check if the email and password match the line of the text file
        if x[0] == email and x[1] == password:
            # Print success message and return to menu
            print("\n===============\nLogged in successfully\n================")
            print("Bringing you back to the main menu\n\n")
            correct = True
            menu()

    # If the email and password dont match any line in the text file print a message and login agian
    if not correct:
        print("Wrong info, try again")
        login()


# Declare the exitProg method
def exitProg():
    # Get the users input
    exitChoice = input("Are you sure you want to exit (y/n)?").lower()
    # Check what the user selected y or n
    if exitChoice == "y":
        # Print message and exit the program
        print("Goodbye!")
        exit(0)
    elif exitChoice == "n":
        # Print message and return to the menu
        print("\nGoing back to menu...\n")
        menu()
    else:
        # Call the method and ask the user again
        exitProg()


# Print welcome message
print("========================================\n"
      "Hello, Welcome to my basic login system\n"
      "========================================")

# pause for 2 seconds
time.sleep(2)
# call the menu method
menu()
