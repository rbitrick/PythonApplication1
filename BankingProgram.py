import os
from turtle import clear

def get_balance(balance):
    os.system("cls")
    print("***********************")
    print(f"Your balance is ${balance:.2f}")
    print("***********************")
    input("Press enter to continue: ")

def deposit():
    os.system("cls")
    validoption = False
    while validoption != True:
        try: # V2 - 03/19/2025 - RB - try/except on non float inputs
            print("***********************")
            amount = float(input("Enter amount to deposit or 0 to exit: "))
            print("***********************")
        except ValueError:
            return 0
        if amount < 0:
            print(f"Invalid option: {amount}")
        elif amount == 0 or amount == "":
            return 0
        else:
            validoption == True
            return amount


def withdraw(balance):
    os.system("cls")
    validoption = False
    while validoption != True:
        try: # V2 - 03/19/2025 - RB - try/except on non float inputs
            print("***********************")
            amount = float(input("Enter amount to withdraw or 0 to exit: "))
            print("***********************")
        except ValueError:
            return 0
        if amount > balance:
            print("Insufficent Funds")
        elif amount < 0:
            print(f"Invalid Option: {amount}") 
        elif amount == 0:
            return 0
        else:
            validoption == True
            return amount

def main(): #testing commits
    balance = float(0)
    is_running = True

    while is_running:
        os.system("cls")
        print("***********************")
        print("Banking Program")
        print("***********************")
        print("1. Get Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Please choose and option (1-4): ")

        if choice == '1':
            get_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            print("Thank you! Have a nice day!")
            is_running = False
        else:
            print("Please enter a valid option")
main()
