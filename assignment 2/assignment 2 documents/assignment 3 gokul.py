import tkinter as tk
from tkinter import ttk
import json

class FinanceTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")
        self.create_widgets()
        self.transactions = self.load_transactions("transactions.json")

    def create_widgets(self):
        # Frame for table and scrollbar
        self.frame=ttk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH,expand=True)

        # Treeview for displaying transactions
        self.treeview=ttk.Treeview(self.frame,columns=("Expense","Date","Amount"),show="headings")
        self.treeview.heading("Expense",text="Type of expense")
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

        self.search_button=ttk.Button(self.root,text="Search",command=self.search_transactions)
        self.search_button.pack(padx=5,pady=5,side=tk.RIGHT)

    def load_transactions(self,filename):
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
                self.treeview.insert("","end",values=(transaction_type,data["Date"],data[str("Amount")]))

    def search_transactions(self):
        # Placeholder for search functionality
        query=self.search_entry.get().lower()
        processed_transactions={}
        for transaction_type,transactions_data in self.transactions.items():
            processed_transactions[transaction_type]=[data for data in transactions_data if query in str(data["Amount"]).lower() or query in transaction_type.lower() or query in data["Date"].lower()]
            

        self.display_transactions(processed_transactions)
        
    def column_click(self,event):
        col_id=self.treeview.identify_column(event.x)
        if col_id:
            col=col_id.split("#")[-1]
            self.treeview_sort_column(col)
        
    def sort_by_column(self, col,reverse=None):
        items=self.treeview.get_children("")
        data=[(self.treeview.set(child.col),child)for child in items]
        data.sort(reverse=False)
        for index,(val,child) in enumerate(data):
            self.treeview.move(child,"",index)
def main():
    root = tk.Tk()
    app = FinanceTrackerGUI(root)
    app.display_transactions(app.transactions)
    root.mainloop()

if __name__ == "__main__":
    main()

