import tkinter as tk
from tkinter import ttk
import json

class FinanceTrackerGUI:
    def __init__(self, root):
        #create a new instance
        self.root = root
        self.root.title("Personal Finance Tracker")
        self.create_widgets()
        self.transactions = self.load_transactions("transactions.json")
        self.treeview.bind("<Button-1>",self.column_click)

    def create_widgets(self):
        # Frame for table and scrollbar
        self.frame=ttk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH,expand=True)

        # Treeview for displaying transactions
        self.treeview=ttk.Treeview(self.frame,columns=("Expense","Date","Amount"),show="headings")
        self.treeview.heading("Expense",text="Type of Expense")
        self.treeview.heading("Date",text="Date")
        self.treeview.heading("Amount",text="Amount")
        self.treeview.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)

        # Scrollbar for the Treeview
        self.scrollbar=ttk.Scrollbar(self.frame,orient=tk.VERTICAL,command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

        # Search bar and button
        self.search_entry=ttk.Entry(self.root)
        self.search_entry.pack(padx=5,pady=5,fill=tk.BOTH)

        #search button
        self.search_button=ttk.Button(self.root,text="Search",command=self.search_transactions)
        self.search_button.pack(padx=5,pady=5,side=tk.RIGHT)

    def load_transactions(self,filename):
        #open the file transactions.json
        try:
            load_file=open(filename,"r")
            transactions=json.load(load_file)
            return transactions
        except FileNotFoundError:
            return {}

    def display_transactions(self,transactions):
        # Remove existing entries
        for entry in self.treeview.get_children():
            self.treeview.delete(entry)
            
        # Add transactions to the treeview
        for transaction_type,transactions_data in self.transactions.items():
            for data in transactions_data:
                self.treeview.insert("","end",values=(transaction_type,data["Date"],data["Amount"]))

    def search_transactions(self):
        # Placeholder for search functionality
        query=self.search_entry.get().lower()
        processed_transactions = {}
        #to search transactions data based from the search query
        for transaction_type,transactions_data in self.transactions.items():
            processed_data=[data for data in transactions_data if
                            query in str(data["Amount"]).lower() or
                            query in transaction_type.lower() or
                            query in data["Date"].lower()]
            if processed_data:
                processed_transactions[transaction_type]=processed_data
            
        
        self.display_transactions(processed_transactions)
        i=1
        for transaction_type,transactions_data in processed_transactions.items():
            print(f"{i}.Expense_type :{transaction_type}")
            j=1
            for details in transactions_data:
                print(f"{j}.Amount :{data['Amount']})\n Date :{data['Date']}")
                j+=1
            i+=1
                  
        
    
    def column_click(self,event):
        #to get column headings for toggle sort
        col_id=self.treeview.identify_column(event.x)
        if col_id:
            col=col_id.split("#")[-1]
            self.sort_by_column(col)
        
    def sort_by_column(self, col,reverse=None):
        #place holder for sorting functioanality
        order=None
        if order == False:
            order = True
        else:
            order = False
            
        items=self.treeview.get_children("")
        data=[(self.treeview.set(child,col),child)for child in items]
        data.sort(reverse=order)
        for index,(val,child) in enumerate(data):
            self.treeview.move(child,"",index)
def main():
    #main function
    root = tk.Tk()
    app = FinanceTrackerGUI(root)
    app.display_transactions(app.transactions)
    root.mainloop()

if __name__ == "__main__":
    main()

