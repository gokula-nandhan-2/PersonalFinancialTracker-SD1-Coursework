import json
from datetime import datetime

# Global list to store transactions
transactions = []

# Function to load transactions from JSON file into the global transactions list
def load_transactions():
    try:
        with open('transactions01.json', 'r') as file:
            global transactions
            # Load transactions from JSON file
            transactions = json.load(file)
    except FileNotFoundError:
        # If file does not exist, start with empty list
        print("No previous transactions found. Starting fresh.")
        transactions = []
    except json.JSONDecodeError:
        # If JSON file is corrupted or invalid, reset list
        print("Error: Invalid JSON format.")
        transactions = []


# Function to save the current transactions list into JSON file
def save_transactions():
    try:
        with open('transactions01.json', 'w') as file:
            file.write('[\n') # Write opening bracket for JSON array
            for i, transaction in enumerate(transactions):
                # Write each transaction list as a JSON string indented by 4 spaces
                file.write('    ' + json.dumps(transaction))
                if i < len(transactions) - 1:
                    file.write(',\n') # Comma after each but last transaction
                else:
                    file.write('\n')
            file.write(']\n') # Write closing bracket for JSON array
        print("Transactions saved successfully!")
    except IOError:
        # Handle file write errors
        print("Error saving transactions")



# Feature implementations

# Function to add a new transaction from user input
def add_transaction():
   while True:
        print("\nEnter Transaction Details!")

        # Get amount, validate it's a non-negative integer
        try:
            amount = int(input("\nEnter the amount: "))
            if amount < 0:
                print("Negative value does not get for an amount!")
                continue
        except ValueError as amount_error:
            print(f"Invalid input for amount: {amount_error}")
            continue

        # Get category as string
        catogory = input("\nEnter the category: ").capitalize()

        # Get transaction type as integer (1 for Income, 2 for Expense)
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

        # Get date in YYYY-MM-DD format and validate it# Get date string and validate format (YYYY-MM-DD)            
        date = input("\nEnter the date (YYYY-MM-DD): ")
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format!")
            continue

        # Create transaction record as list and append to global list
        transaction = [amount, catogory, transaction_type, date]
        transactions.append(transaction)
        print("Transaction added successfully!")
        save_transactions() # Save updated transactions list to file
        break # Exit the input loop after successful add


# Function to display all transactions to the user
def view_transactions():
   if not transactions:
        print("No transactions to view!")
   else:
        count = 1
        print("\nTransactions:")
        for transaction in transactions:
            # Print each transaction with index and details
            print(f"{count}) Amount: {transaction[0]}, Category: {transaction[1]}, Type: {transaction[2]}, Date: {transaction[3]}")
            count += 1 


# Function to update an existing transaction chosen by use
def update_transaction():
    if not transactions:
        print("No transactions to update!")
    else:
        view_transactions() # Show existing transactions
        while True:
            count = int(input("\nEnter the transaction number to update: "))
            if 1 <= count <= len(transactions):
                while True:
                    print("\n1 - Update Amount")
                    print("2 - Update Category")
                    print("3 - Update Type")
                    print("4 - Update Date")

                    choice = input("\nEnter your choice: ")
                    if choice == '1':
                        # Update amount with validation
                        try:
                            amount = int(input("\nEnter the amount: "))
                            if amount < 0:
                                print("Negative value does not get for an amount!")
                                continue
                            transactions[count - 1][0] = amount
                            print("Amount updated successfully!")
                        except ValueError as amount_error:
                            print(f"Invalid input for amount: {amount_error}")
                            continue
                    elif choice == '2':
                        # Update category string
                        category = input("\nEnter the new category: ")
                        transactions[count - 1][1] = category
                        print("Category updated successfully!")
                    elif choice == '3':
                        # Update transaction type with validation
                        try:
                            transaction_type = int(input("\nEnter the type of transaction(1-Income/2-Expense): "))
                            if transaction_type == 1:
                                transaction_type = "Income"
                            elif transaction_type == 2:
                                transaction_type = "Expense"
                            else:
                                print("Invalid transaction type. Please enter 1 for Income or 2 for Expense.")
                                continue
                            transactions[count - 1][2] = transaction_type
                            print("Transaction type updated successfully!")
                        except ValueError:
                            print("Invalid input for transaction type. Please enter a number.")
                            continue
                    elif choice == '4':
                        # Update date with format validation
                        date = input("\nEnter the date (YYYY-MM-DD): ")
                        try:
                            date_obj = datetime.strptime(date, "%Y-%m-%d")
                            transactions[count - 1][3] = date
                            print("Date updated successfully!")
                        except ValueError:
                            print("Invalid date format!")
                            continue
                    else:
                        print("Invalid choice. Please try again.")
                    # Save changes after update
                    save_transactions()
                    break
            else:
                print("Invalid transaction number. Please try again!")


# Function to delete a transaction selected by user
def delete_transaction():
    if not transactions:
        print("No transactions to delete!")
    else:
        while True:
            view_transactions() # Show all transactions with numbers
            try:
                count = int(input("\nEnter the transaction number to delete: "))
                if 1 <= count <= len(transactions):
                    # Delete transaction from list
                    del transactions[count - 1]
                    print("Transaction deleted successfully!")
                    save_transactions() # Save updated list to file
                    break
                else:
                    print("Invalid transaction number. Please try again!")
            except ValueError:
                print("Invalid input. Please enter a number.")

# Function to display a summary of total income, expense and net balance
def display_summary():
    if not transactions:
        print("No transactions to summarize!")
    else:
        income = 0
        expense = 0
        for transaction in transactions:
            if transaction[2] == "Income":
                income += transaction[0]
            else:
                expense += transaction[0]
        print(f"\nTotal Income: {income}")
        print(f"Total Expense: {expense}")
        print(f"Net Balance: {income - expense}")


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


# Run main_menu if this file is run as the main program
if __name__ == "__main__":
 main_menu()