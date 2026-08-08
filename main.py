# ATM Simulation Management System

from datetime import datetime

account = {
    "name": "Nagarajan",
    "account_no": "10001",
    "pin": "1234",
    "balance": 10000
}

transactions = []


def login():
    for i in range(3):
        pin = input("Enter PIN: ")

        if pin == account["pin"]:
            print("\nLogin Successful!")
            return True

        print("Invalid PIN!")

    print("ATM Blocked. Too many attempts.")
    return False


def balance():
    print("\nAvailable Balance: ₹", account["balance"])


def deposit():
    try:
        amount = float(input("Enter deposit amount: ₹"))

        if amount > 0:
            account["balance"] += amount
            transactions.append(
                f"Deposit ₹{amount} - {datetime.now()}"
            )
            print("Amount deposited successfully!")
        else:
            print("Invalid amount!")

    except ValueError:
        print("Enter a valid amount!")


def withdraw():
    try:
        amount = float(input("Enter withdrawal amount: ₹"))

        if amount <= 0:
            print("Invalid amount!")

        elif amount > account["balance"]:
            print("Insufficient balance!")

        else:
            account["balance"] -= amount
            transactions.append(
                f"Withdraw ₹{amount} - {datetime.now()}"
            )
            print("Please collect your cash.")
            print("Remaining Balance: ₹", account["balance"])

    except ValueError:
        print("Enter a valid amount!")


def account_details():
    print("\n----- Account Details -----")
    print("Name       :", account["name"])
    print("Account No :", account["account_no"])
    print("Balance    : ₹", account["balance"])


def transaction_history():
    print("\n----- Transaction History -----")

    if not transactions:
        print("No transactions found.")
    else:
        for transaction in transactions:
            print(transaction)


def change_pin():
    old_pin = input("Enter old PIN: ")

    if old_pin == account["pin"]:
        new_pin = input("Enter new 4-digit PIN: ")

        if len(new_pin) == 4 and new_pin.isdigit():
            account["pin"] = new_pin
            print("PIN changed successfully!")
        else:
            print("PIN must contain 4 digits.")
    else:
        print("Incorrect PIN!")


def atm_menu():

    while True:
        print("\n========== ATM MENU ==========")
        print("1. Account Details")
        print("2. Check Balance")
        print("3. Cash Deposit")
        print("4. Cash Withdrawal")
        print("5. Transaction History")
        print("6. Change PIN")
        print("7. Exit")
        print("===============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_details()

        elif choice == "2":
            balance()

        elif choice == "3":
            deposit()

        elif choice == "4":
            withdraw()

        elif choice == "5":
            transaction_history()

        elif choice == "6":
            change_pin()

        elif choice == "7":
            print("\nThank you for using ATM!")
            break

        else:
            print("Invalid choice!")


def main():
    print("================================")
    print("   ATM SIMULATION MANAGEMENT")
    print("================================")

    if login():
        atm_menu()


if __name__ == "__main__":
    main()