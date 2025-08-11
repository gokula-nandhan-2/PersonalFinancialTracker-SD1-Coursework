import json
from datetime import datetime

# Global dictionary to store transactions
transactions = {}



'''File handling functions'''

# Function to load transactions from a JSON file
def load_transactions():
    try:
        global transactions
        # Open the JSON file for reading
        file = open("transactions02.json", "r")
        # Load transactions data into the global dictionary
        transactions = json.load(file)
        file.close()
        print("Transactions loaded successfully!")
    except FileNotFoundError:
        # If the JSON file does not exist, initialize an empty dictionary
        print("No previous transactions found, starting fresh!")
        transactions = {}
    except json.JSONDecodeError:
        # If JSON file is corrupted or empty, also start fresh
        print("Error decoding JSON file, starting fresh!")
        transactions = {}

        
# Function to save transactions to a JSON file
def save_transactions():
    try:
        # Open the JSON file for writing
        file = open("transactions02.json", "w")
        # Dump the current transactions dictionary into the file
        json.dump(transactions, file, indent=4)
        file.close()
        print("Transactions saved successfully!")
    except IOError:
        # Handle file I/O errors
        print("Error saving transactions to file!")


    
# Read transactions from a text file and add them to the global dictionary
def read_bulk_transactions_from_file(file_name="transactions02.txt"):
    try:
        # Use 'with' to automatically close the file after reading
        with open(file_name, "r") as file:
            for line in file:
                line = line.strip()  # Remove trailing newline and spaces
                if not line:  # Skip empty lines
                    continue
                
                parts = line.split(",")  # Split line by commas
                
                # Validate that the line has exactly 3 parts: type, amount, date
                if len(parts) != 3:
                    print(f"Skipping malformed line: {line}")
                    continue
                
                transaction_type, amount, date = parts
                
                try:
                    # Clean and normalize transaction type text
                    transaction_type = transaction_type.strip().capitalize()
                    # Convert amount to integer
                    amount = int(amount)
                    # Validate date format is YYYY-MM-DD
                    datetime.strptime(date, "%Y-%m-%d")
                except ValueError:
                    # If amount is not int or date format invalid, skip this line
                    print(f"Invalid amount or date format in line: {line}")
                    continue
                
                # Add transaction to dictionary, append if key exists else create new list
                if transaction_type in transactions:
                    transactions[transaction_type].append({"Amount": amount, "Date": date})
                else:
                    transactions[transaction_type] = [{"Amount": amount, "Date": date}]
        
        print("Bulk transactions loaded successfully!")
        # Save transactions after loading from file
        save_transactions()
    except FileNotFoundError:
        # If text file doesn't exist, notify the user
        print("File not found!")



'''Feature implementations'''

# Add a new transaction to global dictionary
def add_transaction():
    while True:
        print("\nEnter Transaction Details!")
        # Input transaction category/type
        expense = input("\nEnter the type of expense :").capitalize()

        try:
            # Input amount and convert to integer
            amount = int(input("\nEnter the amount: "))
            if amount < 0:
                print("Negative value does not get for an amount!")
                continue
        except ValueError as amount_error:
            # Handle invalid input for amount
            print(f"Invalid input for amount: {amount_error}")
            continue

        # Input date and validate format
        date = input("\nEnter the date(YYYY-MM-DD) :")
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format!")
            continue

        # If category does not exist, create it
        if expense not in transactions:
            transactions[expense] = []

        # Append the new transaction entry
        transactions[expense].append({"Amount": amount, "Date": date})
        print("\nTransaction added successfully!")
        # Save updated transactions to JSON file
        save_transactions()
        break  # Exit after successful addition



# View all transactions stored in global dictionary
def view_transactions():
    if not transactions:  # Check if dictionary is empty
        print("No more transactions to view!")
    else:
        print("\n---Transactions---")
        count01 = 1  # Counter for categories
        count02 = 1  # Counter for transaction entries within a category
        for expense in transactions:
            print(f"\n{count01}.{expense}")
            count01 += 1
            for expense_details in transactions[expense]:
                print(f"    {count02} -> Amount: {expense_details['Amount']}, Date: {expense_details['Date']}")
                count02 += 1
                # Reset count02 after each category to keep numbering consistent
                if count02 > len(transactions[expense]):
                    count02 = 1



# Function to update an existing transaction in global dictionary
def update_transaction():
    if not transactions:
        print("No transactions to update!")
    else:
        # Show all transactions with indexes
        view_transactions()

        # Select transaction type by index number
        while True:
            try:
                type_index = int(input("\nEnter the transaction type number to update: ")) - 1
                if not (0 <= type_index < len(transactions)):
                    raise IndexError
                # Get transaction type key from dictionary keys list by index
                transaction_type = list(transactions.keys())[type_index]
                break
            except (ValueError, IndexError):
                print("Invalid selection. Please enter a valid number.")

        details = transactions[transaction_type]
        print(f"\nSelected: {transaction_type}")
        # List all entries under this transaction type
        for idx, entry in enumerate(details, 1):
            print(f"  {idx} -> Amount: {entry['Amount']}, Date: {entry['Date']}")

        # Choose what to update
        print("\n1 - Update Transaction Type")
        print("2 - Update Amount")
        print("3 - Update Date")
        print("4 - Update Both Amount and Date")

        while True:
            choice = input("Your choice: ")
            if choice in ['1', '2', '3', '4']:
                break
            else:
                print("Invalid choice. Enter 1, 2, 3 or 4.")

        # Choice 1: Rename Transaction Type
        if choice == '1':
            while True:
                new_type = input("Enter new transaction type: ").capitalize()
                if new_type:
                    if new_type != transaction_type:
                        # Rename key in dictionary
                        transactions[new_type] = transactions.pop(transaction_type)
                        print("Transaction type renamed successfully.")
                    else:
                        print("New type is same as old type. No changes made.")
                    break
                else:
                    print("Type name cannot be empty!")

        # Choice 2 or 4: Update Amount
        if choice == '2' or choice == '4':
            while True:
                try:
                    # Select which entry to update
                    index = int(input("Select entry number to update amount: ")) - 1
                    if not (0 <= index < len(details)):
                        print("Invalid entry number.")
                        continue

                    while True:
                        try:
                            new_amount = int(input("Enter new amount: "))
                            if new_amount > 0:
                                details[index]["Amount"] = new_amount
                                print("Amount updated.")
                                break
                            else:
                                print("Amount must be positive.")
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")

        # Choice 3 or 4: Update Date
        if choice == '3' or choice == '4':
            while True:
                try:
                    # If choice is not '4' (both), ask which entry number to update
                    if not choice == '4':
                        index = int(input("Select entry number to update date: ")) - 1
                        if not (0 <= index < len(details)):
                            print("Invalid entry number.")
                            continue

                    while True:
                        new_date = input("Enter new date (YYYY-MM-DD): ")
                        try:
                            # Validate date format
                            datetime.strptime(new_date, "%Y-%m-%d")
                            details[index]["Date"] = new_date
                            print("Date updated.")
                            break
                        except ValueError:
                            print("Invalid date format. Please use YYYY-MM-DD.")
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")

        # Save changes
        save_transactions()


        
# Delete a transaction from global dictionary
def delete_transaction():
    if not transactions:
        print("No more transactions to delete!")
    else:
        # Show all transactions with indexes
        view_transactions()
        transaction_type = input("\nEnter type of your expense :").capitalize()
        if transaction_type in transactions:
            while True:
                try:
                    # Select specific entry to delete by index
                    number = int(input("Enter number of specific transaction detail: "))
                    if 0 <= number - 1 < len(transactions[transaction_type]):
                        # Delete the selected transaction entry
                        del transactions[transaction_type][number - 1]
                        print("Transaction deleted successfully!")
                        save_transactions()
                        break
                    else:
                        print("Invalid index. Please try again!")
                except ValueError as error:
                    print(error)
        else:
            print("Type of expense not found!")



# Function to display summary of total expenses by category
def display_summary():
    if not transactions:
        print("No transactions to summarize!")
    else:
        total_expense = 0
        print("\n--- Expense Summary by Category ---\n")
        # Iterate over each transaction category and its entries
        for transaction_type, entries in transactions.items():
            # Sum the amounts in the entries list
            category_total = sum(entry["Amount"] for entry in entries)
            total_expense += category_total
            # Print the category total and number of transactions, handling plural 's'
            print(f"{transaction_type}: {category_total} -> {len(entries)} transaction{'s' if len(entries) != 1 else ''}")   
        print("\nTotal: ", total_expense)



# Main user interaction loop
def main_menu():
    # Load existing transactions from file at program start
    load_transactions()

    while True:
        print("\n---Personal Finance Tracker---")
        print("\n1 - Add Transaction")
        print("2 - View Transactions")
        print("3 - Update Transaction")
        print("4 - Delete Transaction")
        print("5 - Display Summary")
        print("6 - Read Bulk Transactions from File")
        print("7 - Exit")

        try:
            # Ask for user choice input
            choice = int(input("\nEnter your choice: ").strip())
            if 1 <= choice <= 7:
                # Call respective functions based on choice
                if choice == 1:
                    add_transaction()
                elif choice == 2:
                    view_transactions()
                elif choice == 3:
                    update_transaction()
                elif choice == 4:
                    delete_transaction()
                elif choice == 5:
                    display_summary()
                elif choice == 6:
                    read_bulk_transactions_from_file()
                else:  # choice == 7
                    # Save transactions and exit program
                    save_transactions()
                    print("-EXIT-")
                    break
            else:
                print("Invalid choice. Please try again!")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 7.")



# Program entry point
if __name__ == "__main__":
    main_menu()
