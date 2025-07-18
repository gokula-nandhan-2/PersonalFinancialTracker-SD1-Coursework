import json
from datetime import datetime

# Global list to store transactions
transactions = []

# File handling functions
def load_transactions():
    try:
        with open('transactions01.json', 'r') as file:
            global transactions
            transactions = json.load(file)
    except FileNotFoundError:
        print("No previous transactions found. Starting fresh.")
        transactions = []
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")


def save_transactions():
    try:
        with open('transactions01.json', 'w') as file:
           file.write(json.dumps(transactions))
        print("Transactions saved successfully!")
    except IOError:
        print("Error saving transactions")
    except FileNotFoundError:
        print("File not found while saving transactions.")

# Feature implementations
def add_transaction():
   while True:
        print("\nEnter Transaction Details!")

        try:
            amount = int(input("\nEnter the amount: "))
            if amount < 0:
                print("Negative value does not get for an amount!")
                continue
        except ValueError as amount_error:
            print(f"Invalid input for amount: {amount_error}")
            continue

        catogory = input("\nEnter the category: ")


        try:
            transaction_type = int(input("\nEnter the type of transaction(1-Income/2-Expense): "))
            if transaction_type == 1:
                transaction_type = "Income"
            elif transaction_type == 2:
                transaction_type = "Expense"
            else:
                print("Invalid transaction type. Please enter 1 for Income or 2 for Expense.")
                continue
        except ValueError:
            print("Invalid input for transaction type. Please enter a number.")
            continue
            
        date = input("\nEnter the date (YYYY-MM-DD): ")
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format!")
            continue

        transaction = [amount, catogory, transaction_type, date]
        transactions.append(transaction)
        print("Transaction added successfully!")
        save_transactions()
        break   


def view_transactions():
   if not transactions:
        print("No transactions to view!")
   else:
        count = 0
        print("\nTransactions:")
        for transaction in transactions:
            print(f"Amount: {transaction[0]}, Category: {transaction[1]}, Type: {transaction[2]}, Date: {transaction[3]}") 


def update_transaction():
 pass
def delete_transaction():
 pass
def display_summary():
 pass


def main_menu():
    #call functions to load transactions from file
    load_transactions()

    #main programme loop
    while True:
        print("\n---Personal Finance Tracker---")
        print("\n1 - Add Transaction")
        print("2 - View Transactions")
        print("3 - Update Transaction")
        print("4 - Delete Transaction")
        print("5 - Display Summary")
        print("6 - Exit")

        try:
            #prompt user for call the feature implimentation functions
            choice=int(input("\nEnter your choice:"))
            if 1<=choice<=6:
                if choice==1:
                    add_transaction()
                elif choice==2:
                    view_transactions()
                elif choice==3:
                    update_transaction()
                elif choice==4:
                    delete_transaction()
                elif choice==5:
                    display_summary()
                elif choice==6:
                    save_transactions()
                    print("-EXIT-")
                    break
            else:
                print("Invalid choice.Please try again!")
        except ValueError as error:
            print("Invalid choice.Please try again!")



if __name__ == "__main__":
 main_menu()