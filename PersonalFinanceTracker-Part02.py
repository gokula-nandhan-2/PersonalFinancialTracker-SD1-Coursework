import json
from datetime import datetime

#Global dictionary to store transactions
transactions={}



'''File handling functions'''

#function to load transactions from a json file
def load_transactions():
    try:
        global transactions
        file=open("transactions02.json","r")
        transactions=json.load(file)
        file.close()
        print("Transactions loaded successfully!")
    except FileNotFoundError:
        print("No previous transactions found, starting fresh!")
        transactions = {}
    except json.JSONDecodeError:
        print("Error decoding JSON file, starting fresh!")
        transactions = {}

        
#function to save transactions to a json file
def save_transactions():
    try:
        file=open("transactions02.json","w")
        json.dump(transactions,file)
        file.close()
        print("Transactions saved successfully!")
    except IOError:
        print("Error saving transactions to file!")

    
#read transactions from a text file and add them to global dictionary
def read_bulk_transactions_from_file(file_name="transactions02.txt"):
    try:
        file=open(file_name,"r")
        for line in file:
            transaction_type,amount,date=line.strip().split(",")
            try:
                transaction_type = transaction_type.strip().capitalize()
                amount = int(amount)
                datetime.strptime(date, "%Y-%m-%d")  # validate date format
            except ValueError:
                print(f"Invalid amount or date format in line: {line.strip()}")
                continue
            if transaction_type in transactions:
                transactions[transaction_type].append({"Amount":amount,"Date":date})
            else:
                transactions[transaction_type]=[{"Amount":amount,"Date":date}]
        file.close()
        print("Bulk transactions loaded successfully!")
        save_transactions()
    except FileNotFoundError:
        print("File not found!")
        


'''Feature implementations'''

#add a new transaction to global dictionary
def add_transaction():
    while True:
        print("\nEnter Transaction Details!")
        expense = input("\nEnter the type of expense :").capitalize()

        try:
            amount = int(input("\nEnter the amount: "))
            if amount < 0:
                print("Negative value does not get for an amount!")
                continue
        except ValueError as amount_error:
            print(f"Invalid input for amount: {amount_error}")
            continue

        date=input("\nEnter the date(YYYY-MM-DD) :")
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format!")
            continue

        if expense not in transactions:
            transactions[expense]=[]

        transactions[expense].append({"Amount":amount,"Date":date})
        print("\nTransaction added successfully!")
        save_transactions()
        break  # Exit the loop after successful addition



#view all transactions stored in global dictionary
def view_transactions():
    if not transactions:#empty global dictionary
        print("No more transactions to view!")
    else:
        print("\n---Transactions---")
        count01 = 1
        count02 = 1
        for expense in transactions:
            print(f"\n{count01}.{expense}")
            count01 += 1
            for expense_details in transactions[expense]:
                print(f"    {count02} -> Amount: {expense_details['Amount']}, Date: {expense_details['Date']}")
                count02 += 1
                if count02 > len(transactions[expense]):
                    count02 = 1  # Reset count02 for the next expense type



# #update an existing transaction in the transactions(global dictionary)
# def update_transaction():
#     if not transactions:
#         print("No more transactions to update!")
#     else:
#         view_transactions()
#         while True:
#             try:
#                 count = int(input("\nEnter the transaction number to update: "))
#                 if 1 <= count <= len(transactions):
#                     while True:
#                         print("\n1 - Update Transaction Type")
#                         print("2 - Update Amount")
#                         print("3 - Update Date")
#                         print("4 - Both(Amount and Date)")
#                         choice = input("\nEnter your choice: ")

#                         if choice == '1':
#                             old_type = list(transactions.keys())[count - 1]
#                             new_type = input("Enter new transaction type: ").capitalize()
#                             transactions[new_type] = transactions.pop(old_type)
#                             print("Transaction type updated successfully!")
#                             break
#                         elif choice == '2' or choice == '4':
#                             transaction_type = list(transactions.keys())[count - 1]
#                             if transaction_type in transactions:
#                                 number = int(input("Enter number of specific transaction detail: "))
#                                 if 0 <= number - 1 <= len(transactions[transaction_type]):
#                                     try:
#                                         new_amount=int(input("Enter new amount :"))
#                                         if new_amount > 0:
#                                             transactions[transaction_type][count-1]["Amount"]=new_amount
#                                             print("Amount updated successfully!")
#                                     except ValueError as new_amount_error:
#                                         print(new_amount_error)
#                                 else:
#                                     print("Negative or non-identity number does not get for an amount!")
#                             else:
#                                 print("Transaction type not found!")
#                         if choice == '3' or choice == '4':
#                             transaction_type = list(transactions.keys())[count - 1]
#                             if transaction_type in transactions:
#                                 number = int(input("Enter number of specific transaction detail: "))
#                                 if 0 <= number - 1 < len(transactions[transaction_type]):
#                                     new_date=input("Enter new date(YYYY-MM-DD) :")
#                                     try:
#                                         date_obj = datetime.strptime(new_date, "%Y-%m-%d")
#                                         transactions[transaction_type][count-1]["Date"]= new_date
#                                         print("Date updated successfully!")
#                                     except ValueError:
#                                         print("Invalid date format!")
#                                 else:
#                                     print("Invalid number.Please try again!")
#                             else:
#                                 print("Transaction type not found!")                                                
#                         else:
#                             print("Invalid choice. Please try again!")
#                             continue  # Restart the inner loop for valid choice
#                         save_transactions()
#                         break  # Exit the inner loop after successful update
#                 else:
#                     print("Invalid transaction number. Please try again!")
#                     continue  # Restart the outer loop for valid transaction number
#             except ValueError:
#                 print("Invalid input! Please enter a valid number.")
#                 continue  # Restart the outer loop for valid input


# from datetime import datetime

# def update_transaction():
#     if not transactions:
#         print("No more transactions to update!")
#     else:
#         view_transactions()
#         while True:
#             try:
#                 count = int(input("\nEnter the transaction type number to update: "))
#                 if 1 <= count <= len(transactions):
#                     transaction_type = list(transactions.keys())[count - 1]
#                     details = transactions[transaction_type]

#                     print(f"\nSelected Transaction Type: {transaction_type}")
#                     for idx, entry in enumerate(details, 1):
#                         print(f"   {idx} -> Amount: {entry['Amount']}, Date: {entry['Date']}")

#                     print("\n1 - Update Transaction Type")
#                     print("2 - Update Amount")
#                     print("3 - Update Date")
#                     print("4 - Update Both (Amount and Date)")
#                     choice = input("Enter your choice: ")

#                     def get_index():
#                         while True:
#                             try:
#                                 index = int(input("Enter the number of the specific transaction detail to update: ")) - 1
#                                 if not (0 <= index < len(details)):
#                                     print("Invalid transaction detail number!")
#                                     continue
#                                 return index
#                             except ValueError:
#                                 print("Invalid number!")
#                                 continue

#                     if choice == '1':
#                         old_type = transaction_type
#                         new_type = input("Enter new transaction type: ").capitalize()
#                         # Move entry to new type
#                         if new_type != old_type:
#                             transactions[new_type] = transactions.pop(old_type)
#                             print("Transaction type updated successfully!")
#                         else:
#                             print("New type is same as old type. No changes made.")
#                     elif choice == '2' or choice == '4':
#                         try:
#                             index = get_index()
#                             new_amount = int(input("Enter new amount: "))
#                             if new_amount > 0:
#                                 transactions[transaction_type][index]["Amount"] = new_amount
#                                 print("Amount updated successfully!")
#                             else:
#                                 print("Amount must be positive.")
#                                 return
#                         except ValueError:
#                             print("Invalid amount input!")
#                             return

#                     if choice == '3' or choice == '4':
#                         index = get_index()
#                         new_date = input("Enter new date (YYYY-MM-DD): ")
#                         try:
#                             datetime.strptime(new_date, "%Y-%m-%d")
#                             transactions[transaction_type][index]["Date"] = new_date
#                             print("Date updated successfully!")
#                         except ValueError:
#                             print("Invalid date format! Expected YYYY-MM-DD.")
#                             return

#                     save_transactions()
#                     break  # Exit after a successful update

#                 else:
#                     print("Invalid transaction type number.")
#             except ValueError:
#                 print("Please enter a valid number.")


from datetime import datetime

def update_transaction():
    if not transactions:
        print("No transactions to update!")
        return

    view_transactions()

    # Select transaction type
    while True:
        try:
            type_index = int(input("\nEnter the transaction type number to update: ")) - 1
            transaction_type = list(transactions.keys())[type_index]
            break
        except (ValueError, IndexError):
            print("Invalid selection. Please enter a valid number.")

    details = transactions[transaction_type]
    print(f"\nSelected: {transaction_type}")
    for idx, entry in enumerate(details, 1):
        print(f"  {idx} -> Amount: {entry['Amount']}, Date: {entry['Date']}")

    # Choose operation
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
                index = int(input("Select entry number to update date: ")) - 1
                if not (0 <= index < len(details)):
                    print("Invalid entry number.")
                    continue

                while True:
                    new_date = input("Enter new date (YYYY-MM-DD): ")
                    try:
                        datetime.strptime(new_date, "%Y-%m-%d")
                        details[index]["Date"] = new_date
                        print("Date updated.")
                        break
                    except ValueError:
                        print("Invalid date format. Please use YYYY-MM-DD.")
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    save_transactions()



              
        
#delete an transaction from global dictionary
def delete_transaction():
    if not transactions:
        print("No more transactions to delete!")
    else:
        view_transactions()
        transaction_type=input("\nEnter type of your expense :").capitalize()
        if transaction_type in transactions:
            while True:
                    try:
                        number = int(input("Enter number of specific transaction detail: "))
                        if 0 <= number - 1 < len(transactions[transaction_type]):
                            del transactions[transaction_type][number - 1]
                            print("Transaction deleted successfully!")
                            save_transactions()
                            break
                        else:
                            print("Invalid index.Please try again!")
                    except ValueError as error:
                        print(error)
        else:
            print("Type of expense not found!")
    
#function for display summary of total expenses
def display_summary():
    total_expense=0
    for transaction_type in transactions:
        for sub_transaction_dictionary in transactions[transaction_type]:
            total_expense+=sub_transaction_dictionary["Amount"]
    print("Your total expense is",total_expense)
    

#user interactional function
def main_menu():
    #call functions to load transactions from file
    load_transactions()
    read_bulk_transactions_from_file()

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
                else:
                    choice==6
                    save_transactions()
                    print("-EXIT-")
                    break
            else:
                print("Invalid choice.Please try again!")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6.")


#programme start and calling for main menu function
if __name__=="__main__":
    main_menu()
        
    
        
