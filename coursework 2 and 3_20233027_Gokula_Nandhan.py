import json
import tkinter as tk
from coursework_3_20233027 import FinanceTrackerGUI



#Global dictionary to store transactions
transactions={}



'''File handling functions'''

#function to load transactions from a json file
def load_transactions():
    global transactions
    load_file=open("transactions.json","r")
    transactions=json.load(load_file)
    load_file.close()
    print("Transactions loaded successfully!")

        
#function to save transactions to a json file
def save_transactions():
    save_file=open("transactions.json","w")
    json.dump(transactions,save_file)
    save_file.close()
    print("Transactions saved successfully!")

    
#read transactions from a text file and add them to global dictionary
def read_bulk_transactions_from_file(expense="expense.txt"):
    try:
        text_file=open(expense,"r")
        for values in text_file:
            transaction_type,amount,date=values.strip().split(",")
            if transaction_type in transactions:
                transactions[transaction_type].append({"Amount":float(amount,2),"Date":date})
            else:
                transactions[transaction_type]=[{"Amount":float(amount,2),"Date":date}]
    except FileNotFoundError:
        print("File not found!")
        


'''Feature implementations'''

#add a new transaction to global dictionary
def add_transaction():
    print("\nEnter Transaction Details!")
    transaction_type=input("\nEnter the type of expense :")

    while True:
        try:
            amount=float(input("\nEnter the amount :"))
            if amount>=0:
                break
            else:
                print("Negative value does not get for an amount!")
        except ValueError as amount_error:
            print(amount_error)

    date=input("\nEnter the date(YYYY-MM-DD) :")

    if transaction_type not in transactions:
        transactions[transaction_type]=[]

    transactions[transaction_type].append({"Amount":amount,"Date":date})
    print("\nTransaction added successfully!")
    save_transactions()



#view all transactions stored in global dictionary
def view_transactions():
    if not transactions:#empty global dictionary
        print("No more transactions to view!")
    else:
        for transaction_type in transactions:
            print(transaction_type)
            for sub_transaction_dictionary in transactions[transaction_type]:
                print(sub_transaction_dictionary)

                
#update an existing transaction in the transactions(global dictionary)
def update_transaction():
    if not transactions:
        print("No more transactions to update!")
    else:
        print("check Transaction type and index you want to update!")
        view_transactions()
        print("\nNow you can update it!")

        transaction_type=input("\nEnter type of your expense :")
        if transaction_type in transactions:
            while True:
                try:
                    index=int(input("Enter index from purticular type of expense :"))
                    if 0 <= index <len(transactions[transaction_type]):
                        break
                    else:
                        print("Invalid index.Please try again!")
                except ValueError as error:
                    print(error)
                
                
            while True:
                try:
                    new_amount=float(input("Enter new amount :"))
                    if new_amount >= 0:
                        break
                    else:
                        print("Negative value does not get for an amount!")
                except ValueError as new_amount_error:
                    print(new_amount_error)


            new_date=input("Enter new date(YYYY-MM-DD) :")

            #will update new date and amount in nested dictionaries
            transactions[transaction_type][index]["Amount"]=new_amount
            transactions[transaction_type][index]["Date"]=new_date

            print("Transaction updated successfully!")
            save_transactions()
        else:
            print("Transaction not found!")
    
#delete an transaction from global dictionary
def delete_transaction():
    if not transactions:
        print("No more transactions to delete!")
    else:
        print("check Transaction type and index you want to delete!")
        view_transactions()
        print("\nNow you can delete it!")

        transaction_type=input("\nEnter type of your expense :")
        if transaction_type in transactions:
            while True:
                    try:
                        index = int(input("Enter index from purticular type of expense :"))

                        if 0 <= index < len(transactions[transaction_type]):
                            del transactions[transaction_type][index]
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
    
def view_GUI():
    root=tk.Tk()
    app=FinanceTrackerGUI(root)
    app.display_transactions(app.transactions)
    root.mainloop()
    
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
    print("7 - GUI")

    try:
        #prompt user for call the feature implimentation functions
        choice=int(input("\nEnter your choice:"))
        if 1<=choice<=7:
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
            elif choice==7:
                view_GUI()
        else:
            print("Invalid choice.Please try again!")
    except ValueError as error:
        print(error)

#display the GUI
def view_GUI():
    root=tk.Tk()
    app=FinanceTrackerGUI(root)
    app.display_transactions(app.transactions)
    root.mainloop()

    
#programme start and calling for main menu function
if __name__=="__main__":
    main_menu()
        
    
        
